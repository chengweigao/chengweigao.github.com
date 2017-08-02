#!/bin/bash
#by chengwigao
#使用脚本生成js文档目录
python dirToJson.py;
#git提交文件
git add -A;
git add .;
#定义提交备注
DATEFORMATTYPE1=$(date +%Y%m%d%H%M);
git commit -m "${DATEFORMATTYPE1}";
#推送提交
git push;


