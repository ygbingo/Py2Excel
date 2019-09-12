# 从query中提取slots值

### 项目文件说明
- slots.xlsx: 存放词槽(根据权重，优先级从高致低排列)
    - sheet：为slot名
    - value列：slot内容
    - slots：slot值

- query.xlsx: 待提取文件
    - 意图编号*：必填
    - query*：必填
    - slots：选填(可能被覆盖)
    - 备注：选填

- result.xls: 输出文件(如果不存在，会自动创建)
    - 意图编号*
    - query*
    - slots
    - 备注
    
### 08/05
1、优化显示过程；<br>
2、优化单一词槽后有分号；