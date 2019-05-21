# -*- coding: utf-8 -*-
"""
Created on 2018/8/1

@author: xing yan
"""
from random import shuffle, sample, randint, choice

administrative_div_code = ['110101', '110102', '110105', '110106', '110107', '110108', '110109', '110111', '110112', '110113', '110114', '110115', '110116', '110117', '110118', '110119']

surname = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楮', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闽', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '麹', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '斜', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '郁', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '郤', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东', '欧', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '后', '荆', '红', '游', '竺', '权', '逑', '盖', '益', '桓', '公', '晋', '楚', '阎', '法', '汝', '鄢', '涂', '钦', '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '商', '牟', '佘', '佴', '伯', '赏', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟']

double_surname = ['万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '锺离', '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '丌官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓拔', '夹谷', '宰父', '谷梁', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '梁丘', '左丘', '东门', '西门', '南宫']

how_name = ['强', '志', '艺', '锦', '朗', '新', '义', '固', '毅', '鹏', '舒', '浩', '寒', '黛', '纯', '生', '成', '彪', '青', '有', '功', '鸣', '承', '哲', '士', '飘', '榕', '馨', '邦', '顺', '娥', '斌', '雪', '园', '竹', '明', '力', '维', '海', '滢', '树', '冰', '影', '荔', '荣', '裕', '昭', '仪', '盛', '克', '康', '香', '伯', '宁', '壮', '瑾', '利', '林', '振', '瑶', '枝', '琴', '岚', '彩', '萍', '凝', '仁', '融', '梁', '琰', '琬', '思', '军', '朋', '全', '贵', '先', '欢', '凡', '芳', '真', '德', '惠', '冠', '嘉', '旭', '露', '慧', '俊', '婕', '丹', '娣', '松', '梦', '卿', '勤', '钧', '磊', '瑞', '光', '华', '可', '澜', '琛', '春', '莲', '丽', '武', '宁', '时', '月', '晨', '达', '民', '超', '琳', '琼', '雁', '辉', '环', '福', '霄', '英', '红', '芸', '才', '佳', '爱', '苑', '芝', '馥', '素', '霞', '昌', '莉', '兰', '行', '波', '震', '广', '伟', '怡', '咏', '国', '莺', '婷', '纨', '家', '飞', '菁', '洁', '之', '刚', '绍', '珠', '学', '君', '诚', '芬', '思', '巧', '淑', '腾', '桂', '娟', '云', '涛', '良', '贞', '勇', '伊', '翰', '聪', '兴', '毓', '富', '山', '东', '群', '彬', '秋', '妹', '蕊', '媛', '言', '翠', '晶', '保', '星', '玲', '婉', '颖', '策', '欣', '会', '娴', '燕', '羽', '坚', '翔', '致', '珍', '龙', '宏', '奇', '艳', '希', '善', '筠', '亨', '峰', '进', '友', '弘', '亚', '凤', '茗', '娅', '秀', '航', '厚', '启', '建', '胜', '安', '柔', '祥', '玉', '敬', '梅', '河', '庆', '璐', '泰', '泽', '瑗', '心', '娜', '和', '栋', '健', '杰', '育', '平', '蓓', '子', '亮', '发', '博', '姬', '莎', '楠', '珊', '若', '静', '元', '轮', '信', '枫', '伦', '政', '豪', '天', '茂', '晓', '悦', '风', '永', '霭', '叶', '美', '姣', '宜', '世', '菲', '辰', '婵', '文', '炎', '雅', '璧', '菊', '雄', '江', '中', '薇', '妍', '谦', '韵', '茜', '清', '爽', '琦', '岩', '蓉', '乐', '倩', '以', '眉', '荷']

small_name = ['秋', '官', '佳', '尔', '天', '运', '公', '星', '晋', '西', '宛', '宗', '萌', '夜', '卷', '月', '珠', '豪', '易', '真', '若', '郑', '灿', '斌', '雅', '嘉', '奕', '一', '昕', '夏', '哲', '鸣', '宏', '蔚', '晶', '恒', '观', '盼', '榕', '锐', '寻', '睿', '晓', '莘', '紫', '渊', '子', '明', '思', '施', '添', '暄', '竹', '灵', '欣', '姚', '汝', '鹏', '玥', '浩', '彦', '德', '孔', '雨', '淑', '诗', '曼', '昔', '寒', '陀', '秦', '杰', '福', '润', '幻', '华', '顺', '笛', '又', '畅', '雁', '语', '瑜', '旭', '立', '尤', '璐', '舞', '言', '逸', '水', '承', '爱', '云', '强', '书', '玉', '丘', '晨', '安', '韵', '钟', '清', '州', '文', '泽', '辰', '瑞', '博']

name = ['茜', '画', '涵', '瓜', '蕊', '鸣', '园', '枫', '嘉', '莹', '文', '洋', '秀', '锐', '官', '佳', '政', '依', '雁', '祝', '杨', '悦', '丙', '璇', '顾', '林', '洁', '莎', '乐', '婉', '庆', '宛', '华', '彤', '昔', '合', '洪', '爱', '淼', '丽', '甜', '巧', '越', '闵', '果', '沛', '晶', '冉', '耿', '霞', '里', '怀', '易', '春', '汕', '远', '昊', '卉', '杰', '辰', '堂', '城', '池', '又', '光', '西', '谷', '豪', '赫', '璐', '松', '梅', '汝', '冰', '溶', '琪', '润', '如', '滢', '位', '醒', '尚', '霖', '泽', '俊', '溪', '鑫', '青', '子', '道', '国', '乙', '玉', '呈', '臻', '伽', '钰', '菡', '孔', '观', '罗', '馨', '惠', '轩', '栾', '翔', '暄', '建', '月', '言', '琴', '寒', '涛', '帆', '元', '晗', '东', '敏', '慧', '昆', '音', '珠', '祥', '苗', '栋', '宜', '君', '萌', '晴', '玥', '曼', '贤', '花', '美', '致', '钟', '源', '彦', '充', '落', '若', '守', '怡', '夏', '晨', '丘', '思', '齐', '屏', '安', '傲', '钗', '哲', '蓝', '天', '菲', '诗', '毅', '慈', '妍', '公']

full_surname = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楮', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闽', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '麹', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '斜', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '郁', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '郤', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东', '欧', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '后', '荆', '红', '游', '竺', '权', '逑', '盖', '益', '桓', '公', '晋', '楚', '阎', '法', '汝', '鄢', '涂', '钦', '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '商', '牟', '佘', '佴', '伯', '赏', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '锺离', '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '丌官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓拔', '夹谷', '宰父', '谷梁', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '梁丘', '左丘', '东门', '西门', '南宫']

full_name = ['霖', '秦', '桂', '瑾', '奕', '茜', '永', '博', '贤', '洪', '官', '汝', '志', '舒', '瑶', '贵', '昆', '良', '冉', '闵', '光', '新', '义', '佳', '美', '秋', '婉', '屏', '仪', '全', '淼', '一', '亨', '孔', '勇', '浩', '又', '钧', '生', '珊', '菲', '伦', '可', '荣', '晓', '菡', '力', '露', '堂', '易', '滢', '有', '瑜', '琴', '树', '曼', '天', '言', '赫', '发', '馨', '中', '超', '琳', '琪', '健', '固', '瓜', '陀', '澜', '媛', '尔', '丽', '振', '刚', '尤', '山', '士', '旭', '园', '倩', '致', '栾', '行', '艺', '画', '落', '蔚', '芳', '榕', '河', '晴', '航', '观', '楠', '启', '承', '民', '灵', '鸣', '香', '梅', '嘉', '栋', '安', '林', '婕', '艳', '信', '时', '郑', '菊', '克', '语', '韵', '瑗', '敬', '燕', '傲', '策', '彤', '幻', '东', '溪', '娟', '薇', '星', '进', '枝', '卉', '豪', '灿', '裕', '冠', '呈', '元', '慈', '君', '里', '莉', '凝', '轮', '鹏', '茗', '杰', '雄', '婵', '巧', '保', '芸', '平', '娣', '子', '娜', '霭', '哲', '厚', '位', '纯', '寒', '静', '达', '风', '卿', '润', '腾', '莘', '夏', '渊', '波', '琰', '霄', '雅', '翔', '丹', '菁', '冰', '羽', '翠', '海', '强', '笛', '祥', '罗', '辰', '芝', '娥', '黛', '晶', '国', '岩', '妍', '盛', '道', '淑', '英', '甜', '勤', '如', '姚', '晋', '书', '苗', '鑫', '德', '慧', '添', '文', '玥', '兴', '姬', '震', '华', '雁', '政', '锐', '乙', '怀', '琦', '娴', '蓓', '莺', '诚', '若', '昔', '洋', '姣', '彩', '才', '睿', '合', '池', '莲', '荷', '龙', '仁', '源', '柔', '雨', '明', '卷', '玉', '坚', '成', '融', '花', '昊', '耿', '伟', '奇', '水', '颖', '梦', '朗', '悦', '琬', '思', '乐', '聪', '宛', '锦', '尚', '萍', '莎', '彪', '真', '雪', '舞', '蓝', '诗', '珍', '伽', '婷', '善', '蕊', '宁', '春', '芬', '毓', '充', '红', '炎', '珠', '莹', '环', '斌', '清', '胜', '壮', '彦', '影', '昭', '运', '友', '盼', '敏', '暄', '沛', '汕', '萌', '宜', '竹', '杨', '齐', '琛', '心', '彬', '宗', '越', '涵', '纨', '庆', '晗', '瑞', '醒', '俊', '秀', '谦', '顾', '磊', '泰', '依', '涛', '世', '枫', '臻', '果', '爽', '茂', '轩', '惠', '功', '璧', '丘', '远', '素', '州', '逸', '苑', '钰', '守', '弘', '维', '溶', '凡', '绍', '育', '亚', '富', '伯', '立', '毅', '先', '恒', '寻', '施', '爱', '丙', '荔', '晨', '和', '军', '钟', '璐', '妹', '朋', '邦', '希', '飘', '畅', '亮', '叶', '飞', '武', '咏', '梁', '洁', '公', '馥', '紫', '筠', '青', '祝', '松', '辉', '家', '康', '娅', '之', '翰', '钗', '璇', '以', '欣', '岚', '福', '蓉', '建', '宏', '泽', '利', '江', '兰', '谷', '群', '昕', '帆', '峰', '月', '城', '音', '广', '凤', '夜', '玲', '伊', '欢', '怡', '霞', '云', '琼', '西', '学', '昌', '会', '顺', '眉', '贞']



print(administrative_div_code)