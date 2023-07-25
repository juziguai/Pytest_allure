import requests, jsonpath, pytest, ast, os, allure, time, webbrowser, subprocess
from xToolkit import xfile
from string import Template
from Utils.parameter_dict import parameter_dict

"""
Created by: juzi
Created time: 2023/6/5 1:17 
Purpose:
"""
# 读取测试用例文档
testSuite = xfile.read("接口测试用例.xls").excel_to_dict(sheet=0)

# 创建以时间戳命名的文件夹
timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())


# pytest装饰器 循环读取测试用例文档内容 自带循环 遍历数据  括号内的含义  变量名，数据
@pytest.mark.parametrize("case_info", testSuite)
def test_requests(case_info):
    url = case_info["请求url"]
    text_dict = parameter_dict().show_parameter()
    print("保存的参数字典：", text_dict)
    if "$" in url:
        url = Template(url).substitute(text_dict)
    api_url = case_info["host参数"] + url
    api_method = case_info["请求方式"]
    api_params = case_info["url携带参数"]
    api_data = case_info["data参数"]
    api_headers = case_info["请求头参数"]
    api_code = case_info["预期响应码"]
    if "$" in api_data:
        api_data = Template(api_data).substitute(text_dict)
    api_response = requests.request(
        url=api_url,
        data=eval(api_data),
        headers=ast.literal_eval(api_headers),
        params=eval(api_params),
        method=api_method)
    # assert login_response.status_code == 200
    if api_response.status_code == api_code:
        print("状态码断言成功！", api_response.status_code)
    else:
        print("状态码断言失败", api_response.status_code)
    extract_parameters = case_info["提取参数"].strip()
    if extract_parameters != "" or len(extract_parameters) != 0:
        if "," in extract_parameters:
            extract_parameters = ast.literal_eval(extract_parameters)
            for i in extract_parameters:
                response_parameters_data = jsonpath.jsonpath(
                    api_response.json(), "$.." + i)
                # 循环保存需要的参数数据到字典
                parameter_dict().set_parameter(i, response_parameters_data[0])
                print("提取参数：" + i + ":" + response_parameters_data[0] + " 保存字典完毕!")
        else:
            extract_parameters = ast.literal_eval(extract_parameters)
            response_parameters_data = jsonpath.jsonpath(
                api_response.json(), "$.." + extract_parameters)
            # 循环保存需要的参数数据到字典
            parameter_dict().set_parameter(extract_parameters, response_parameters_data[0])
            print("提取参数：" + extract_parameters + "：" + response_parameters_data[0] + " 保存字典完毕!")

    else:
        print("提取参数为空，不做相关提取操作,继续执行下一条案例！")

    print(case_info["用例名称"], "执行完毕！")
    print(api_response.text)

    """
    自动生成测试报告 -- allure 
    """


if __name__ == '__main__':
    # 运行pytest命令并指定保存结果的文件夹
    pytest_command = f"pytest -vs --capture=sys main.py --clean-alluredir --alluredir=allure-results/{timestamp}"
    subprocess.run(pytest_command, shell=True)
    # 保存pytest测试数据到allure-results/下
    serve_command = f"allure generate allure-results/{timestamp} -o allure_html/{timestamp}/ --clean"
    subprocess.run(serve_command, shell=True)
    # 打开浏览器运行测试报告
    file_path = f"http://localhost:63342/接口自动化框架/allure_html/{timestamp}/index.html"  # 替换为你的index.html文件路径
    webbrowser.open(file_path)
