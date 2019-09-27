class get_visit_ip_email():

    # 从nginx日志中获取IP并写入txt文件，同时获取每个IP的频次，并返回一个dict
    def get_ip_from_nginx(self, nginx_file_path):
        result = {}
        ip_list = []
        try:
            with open(nginx_file_path, 'r', encoding='utf8') as f:
                nginx_content = f.readlines()
            with open(nginx_file_path.split('.')[0] + '.txt', 'w', encoding='utf8') as f:
                for line in nginx_content:
                    ip = line.split(' ')[0]
                    print(ip)
                    f.write(ip + '\n')
                    if ip in result.keys():
                        result[ip] += 1
                    else:
                        result[ip] = 1
                    ip_list.append(ip)
            print('提取IP成功！')

            self.number_of_ip(ip_list)
            # 返回每个IP的出现频次
            return result
        except Exception as e:
            print('因为 %s 的原因，从nginx日志中获取ip失败！' % e)

    # 第一种统计list中元素次数的方法，set得到不重复的key，list的count统计出现次数
    def number_of_ip(self, ip_list):
        result = {}
        for i in set(ip_list):
            result[i] = ip_list.count(i)
        print(result)


if __name__ == '__main__':
    get_visit_ip_email = get_visit_ip_email()
    get_visit_ip_email.get_ip_from_nginx('access_9_26.log')
