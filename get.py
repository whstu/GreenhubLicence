import requests

# API Key 已经在代码中硬编码
headers = {
    "Authorization": "Basic cmtfbGl2ZV81MUw5c3JLQ29GamtETjR4UGtvdEs2V0dHUHFmd2tnd3RFNkkxcTFURTlrdktzZ0s3SlQ5Mk5oaUFHeGpKeDQ0ejdHZnBzU1hZNmtpTVkyTTFWWkhFajJZVjAwbjRPS3pUSlg6"
}

def fetch_customers_from_stripe():
    """从 Stripe API 获取客户信息并提取 license_code"""
    try:
        # 发送 GET 请求到 Stripe API
        response = requests.get("https://api.stripe.com/v1/customers", headers=headers)
        
        # 检查响应状态码
        if response.status_code != 200:
            print(f"获取客户数据失败，状态码: {response.status_code}")
            return None

        # 解析 JSON 响应
        result = response.json()

        # 提取每个客户的 license_code
        license_codes = [customer['metadata'].get('license_code', 'No license code') for customer in result.get('data', [])]
        return license_codes

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
        return None

def main():
    # 获取客户的 license_code
    license_codes = fetch_customers_from_stripe()

    if license_codes:
        # 将 license_code 保存到文件
        with open('license_codes.txt', 'w') as file:
            for code in license_codes:
                file.write(f"{code}\n")
    else:
        print("未能获取到客户的 license_code")

if __name__ == "__main__":
    main()
