import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:dio/dio.dart';
import './examStart.dart';

class Exam extends StatefulWidget {
  final String userId;
  Exam(this.userId) {}
  _ExamState createState() => _ExamState(userId);
}

class _ExamState extends State<Exam> {
  final String userId;
  _ExamState(this.userId) {}
  //获得试卷字符串准备传给考试页面，获得用户名和分数等用户信息
  String questions;
  String userInfo;
  var info;
  String score = '0';
  void _getHttp() async {
    try {
      Response response;
      Dio dio = new Dio();
      response = await dio.get("http://192.168.1.102:8000/questions");
      questions = response.data.toString();
      print('questions******' + questions);
      response = await dio
          .get("http://192.168.1.102:8000/get_user", data: {"user_id": userId});
      userInfo = response.data.toString();
      print('userInfo********' + userInfo);
      info = json.decode(userInfo); //转换成map使用用户的具体信息
      setState(() {
        score = info['score'].toString();
      });
    } catch (e) {
      print(e);
    }
  }

  @override
  void initState() {
    super.initState();
    _getHttp();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Column(
        children: <Widget>[
          Padding(
            padding: EdgeInsets.fromLTRB(0, 100, 0, 50),
            child: Text('您上次测试的得分是：'),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(0, 50, 0, 100),
            child: Text('$score 分！'),
          ),
          RaisedButton(
            child: Text('开始测试'),
            onPressed: () {
              Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => ExamStart(userId, questions)))
                  .then((onValue) {
                //返回时带回新成绩
                setState(() {
                  if (onValue != null) {
                    score = onValue;
                  }
                });
              });
            },
          )
        ],
      ),
    ));
  }
}
