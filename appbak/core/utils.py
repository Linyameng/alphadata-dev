# -*- coding: utf-8 -*-
"""
Created on 2018/7/31

@author: xing yan
"""
import datetime
from random import randint, choice, sample


class Fabricate:
    """生成随机客户信息"""

    @staticmethod
    def cust_id(addr_code=None, birth_code=None):
        """
        身份证格式如：ABCDEFYYYYMMDDXXXR

        1. 地址码（ABCDEF）
            登记户口所在地的行政区划代码（省、市、县）

        2. 出生日期（YYYYMMDD）
            居民出生的年月日

        3. 顺序码（XXX）
            同一地址码区域内，同年、月、日出生人的所编订的顺序号，身份证顺序码的奇数分配给男生，偶数给女生

        4. 校验码（R）
            R之前的17位为本地码，R根据本体码，按照校验顺序算法计算出来。

        5. 校验算法
            将本地码各位数字乘以对应的加权因子并求和，除以11得到余数，根据余数通过校验码对照表查得校验码

        6. 加权因子表：
            [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

        7. 校验码表：
            ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

        :return: id
        """

        weight_factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        administrative_div_code = ['420923', '611023', '513324', '411527', '620600', '621123', '530700', '371626',
                                   '450603', '222400', '431026', '360704', '321181', '610929', '610525', '371311',
                                   '440783', '451324', '654201', '130121', '451029', '522700', '140212', '530502',
                                   '445200', '232722', '441700', '130209', '340208', '150924', '210381', '371724',
                                   '110115', '130924', '622925', '360735', '640424', '310000', '542524', '350624',
                                   '510304', '421182', '430623', '341502', '341504', '411522', '542525', '130609',
                                   '520103', '340403']

        address = choice(administrative_div_code) if addr_code is None else addr_code

        try:
            if birth_code is not None and len(birth_code) == 6:
                birth_day = birth_code
            else:
                year, month, day = randint(1970, 2000), randint(1, 12), randint(1, 28)
                d = datetime.date(year, month, day)
                birth_day = d.strftime('%Y%m%d')
        except ValueError:
            print("输入日期格式非, 使用默认19890101")
            birth_day = "19890101"

        order = ('00' + str(randint(1, 999)))[-3:]

        local_number = address + birth_day + order

        weight_sum = sum([int(e) * weight_factor[i] for i, e in enumerate(local_number)])

        check_code = check_code_list[weight_sum % 11]

        return local_number + check_code

    @staticmethod
    def cust_name():
        full_surname = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楮', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                        '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水',
                        '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞',
                        '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕',
                        '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平',
                        '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏',
                        '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闽', '席',
                        '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆',
                        '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘',
                        '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉',
                        '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '麹', '家', '封', '芮',
                        '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷',
                        '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '斜', '厉',
                        '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿',
                        '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '郁', '胥',
                        '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍',
                        '郤', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄',
                        '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖',
                        '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东', '欧',
                        '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚',
                        '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '后', '荆',
                        '红', '游', '竺', '权', '逑', '盖', '益', '桓', '公', '晋', '楚', '阎', '法', '汝', '鄢', '涂', '钦', '岳', '帅',
                        '缑', '亢', '况', '后', '有', '琴', '商', '牟', '佘', '佴', '伯', '赏', '墨', '哈', '谯', '笪', '年', '爱', '阳',
                        '佟']

        double_surname = ['万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政',
                          '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '锺离', '宇文', '长孙', '慕容', '鲜于', '闾丘',
                          '司徒', '司空', '丌官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓拔',
                          '夹谷', '宰父', '谷梁', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '梁丘', '左丘', '东门', '西门',
                          '南宫']

        full_name = ['霖', '秦', '桂', '瑾', '奕', '茜', '永', '博', '贤', '洪', '官', '汝', '志', '舒', '瑶', '贵', '昆', '良', '冉', '闵',
                     '光', '新', '义', '佳', '美', '秋', '婉', '屏', '仪', '全', '淼', '一', '亨', '孔', '勇', '浩', '又', '钧', '生', '珊',
                     '菲', '伦', '可', '荣', '晓', '菡', '力', '露', '堂', '易', '滢', '有', '瑜', '琴', '树', '曼', '天', '言', '赫', '发',
                     '馨', '中', '超', '琳', '琪', '健', '固', '瓜', '陀', '澜', '媛', '尔', '丽', '振', '刚', '尤', '山', '士', '旭', '园',
                     '倩', '致', '栾', '行', '艺', '画', '落', '蔚', '芳', '榕', '河', '晴', '航', '观', '楠', '启', '承', '民', '灵', '鸣',
                     '香', '梅', '嘉', '栋', '安', '林', '婕', '艳', '信', '时', '郑', '菊', '克', '语', '韵', '瑗', '敬', '燕', '傲', '策',
                     '彤', '幻', '东', '溪', '娟', '薇', '星', '进', '枝', '卉', '豪', '灿', '裕', '冠', '呈', '元', '慈', '君', '里', '莉',
                     '凝', '轮', '鹏', '茗', '杰', '雄', '婵', '巧', '保', '芸', '平', '娣', '子', '娜', '霭', '哲', '厚', '位', '纯', '寒',
                     '静', '达', '风', '卿', '润', '腾', '莘', '夏', '渊', '波', '琰', '霄', '雅', '翔', '丹', '菁', '冰', '羽', '翠', '海',
                     '强', '笛', '祥', '罗', '辰', '芝', '娥', '黛', '晶', '国', '岩', '妍', '盛', '道', '淑', '英', '甜', '勤', '如', '姚',
                     '晋', '书', '苗', '鑫', '德', '慧', '添', '文', '玥', '兴', '姬', '震', '华', '雁', '政', '锐', '乙', '怀', '琦', '娴',
                     '蓓', '莺', '诚', '若', '昔', '洋', '姣', '彩', '才', '睿', '合', '池', '莲', '荷', '龙', '仁', '源', '柔', '雨', '明',
                     '卷', '玉', '坚', '成', '融', '花', '昊', '耿', '伟', '奇', '水', '颖', '梦', '朗', '悦', '琬', '思', '乐', '聪', '宛',
                     '锦', '尚', '萍', '莎', '彪', '真', '雪', '舞', '蓝', '诗', '珍', '伽', '婷', '善', '蕊', '宁', '春', '芬', '毓', '充',
                     '红', '炎', '珠', '莹', '环', '斌', '清', '胜', '壮', '彦', '影', '昭', '运', '友', '盼', '敏', '暄', '沛', '汕', '萌',
                     '宜', '竹', '杨', '齐', '琛', '心', '彬', '宗', '越', '涵', '纨', '庆', '晗', '瑞', '醒', '俊', '秀', '谦', '顾', '磊',
                     '泰', '依', '涛', '世', '枫', '臻', '果', '爽', '茂', '轩', '惠', '功', '璧', '丘', '远', '素', '州', '逸', '苑', '钰',
                     '守', '弘', '维', '溶', '凡', '绍', '育', '亚', '富', '伯', '立', '毅', '先', '恒', '寻', '施', '爱', '丙', '荔', '晨',
                     '和', '军', '钟', '璐', '妹', '朋', '邦', '希', '飘', '畅', '亮', '叶', '飞', '武', '咏', '梁', '洁', '公', '馥', '紫',
                     '筠', '青', '祝', '松', '辉', '家', '康', '娅', '之', '翰', '钗', '璇', '以', '欣', '岚', '福', '蓉', '建', '宏', '泽',
                     '利', '江', '兰', '谷', '群', '昕', '帆', '峰', '月', '城', '音', '广', '凤', '夜', '玲', '伊', '欢', '怡', '霞', '云',
                     '琼', '西', '学', '昌', '会', '顺', '眉', '贞']

        if randint(1, 12) % 3 == 0:
            surname = choice(double_surname)
        else:
            surname = choice(full_surname)

        a = randint(1, 16)

        if a % 4 == 0:
            last_name = choice(full_name)
        elif a % 5 == 0:
            last_name = choice(full_name) * 2
        else:
            last_name = sample(full_name, 2)

        return surname + ''.join(last_name)

    @staticmethod
    def phone_number():
        """
        1. 手机号码：
           移动号段：134,135,136,137,138,139,147,150,151,152,157,158,159,170,178,182,183,184,187,188
           联通号段：130,131,132,145,155,156,170,171,175,176,185,186
           电信号段：133,149,153,170,173,177,180,181,189

        :return: phone_number :int
        """
        phone_number_prefix = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158',
                               '159', '170', '178', '182', '183', '184', '187', '188', '130', '131', '132', '145',
                               '155', '156', '170', '171', '175', '176', '185', '186', '133', '149', '153', '170',
                               '173', '177', '180', '181', '189']

        return choice(phone_number_prefix) + str(randint(10000000, 99999999))

    @staticmethod
    def bank_number(end_number=None):
        bank_card_prefix = ['356852', '427030', '622235', '439225', '421869', '518710', '622922', '403361', '552586',
                            '356885', '520083', '356851', '404119', '519413', '622690', '376969', '518212', '622318',
                            '622578', '376968', '622636', '498451', '558730', '552589', '622280', '404738', '622688',
                            '356840', '433668', '552583', '404117', '622581', '622517', '404172', '622655', '523036',
                            '481699', '433666', '645621', '528709', '403392', '622161', '356889', '403391', '404739',
                            '438088', '404171', '404158', '622188', '520108']
        if end_number is None:
            end_number = '111'
        return choice(bank_card_prefix) + str(randint(1000000, 9999999999)) + end_number

    def get_more_generate(self, num, end_number):
        return [(self.cust_id(), self.cust_name(), self.phone_number(), self.bank_number(end_number)) for n in range(num)]


if __name__ == '__main__':
    print(Fabricate())
