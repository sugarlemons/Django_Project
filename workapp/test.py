view_name = "Joe Bidden"
view_relationship = [["妻子", "吉尔·拜登"],
                     ["儿子", "亨特·拜登"],
                     ["儿子", "傅·拜登"],
                     ["弟弟", "詹姆斯·拜登"]]  # 关系不固定有几个，而且可能有好几个儿子，所以用字典的时候可能会有重名的问题
view_label = {"sports": 0,
              "foods": 0,
              "politic": 1,
              "military": 1}  # 这些标签是固定的，用0/1代表有/没有，

chart_options = {
    'title': 'ECharts 入门示例',
    'legend': ['销量'],
    'xAxis:': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
    'series': ['销量', 'bar', [5, 20, 36, 10, 10, 20]]  # name type data
}

result = {"name": view_name,
          "relationship": view_relationship,  # 前端直接relationship.key的名字即可提取
          "label": view_label,
          "option": chart_options
          }
print(type(result))
