import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:dio/dio.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:flutter/rendering.dart';

class Question {
  final String number;
  final String question;
  final List answers;
  final String answer;
  Question(this.number, this.question, this.answers, this.answer);
}

class ExamStart extends StatefulWidget {
  final String userId, questions;
  ExamStart(this.userId, this.questions) {}
  _ExamStartState createState() => _ExamStartState(userId, questions);
}

class _ExamStartState extends State<ExamStart> {
  final String userId, questions;
  _ExamStartState(this.userId, this.questions) {}
  List _result = [];
  int _index = 0;
  List<Question> _questions = List();
  String _score = '';
  bool _showLoading = false;
  String _newValue = "";
  String _raisedButton = '下一题';
  bool _showScoreDialog = false;

  void _getHttp() async {
    try {
      Response response;
      Dio dio = new Dio();
      response = await dio.get("http://192.168.1.102:8000/exam",
          data: {"user_id": userId, "result": _result.toString()});
      setState(() {
        _score = response.data.toString();
      });
    } catch (e) {
      print(e);
    }
  }

  Future _scoreRequest() async {
    return Future.delayed(Duration(seconds: 3), () {});
  }

  void _submit() {
    if (_newValue == '') {
      showDialog<Null>(
        context: context,
        barrierDismissible: false,
        builder: (BuildContext context) {
          return new AlertDialog(
            title: new Text('警告：'),
            content: new SingleChildScrollView(
              child: new ListBody(
                children: <Widget>[
                  new Text('请选择一个答案！'),
                ],
              ),
            ),
            actions: <Widget>[
              new FlatButton(
                child: new Text('确定'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        },
      );
    } else {
      if (_result.length < _questions.length) {
        _result.add(_newValue);
      }
      debugPrint('result************' + _result.toString());
      if (_index + 1 < _questions.length) {
        setState(() {
          _index = _index + 1;
        });
        _newValue = '';
      }
      if (_index + 1 == _questions.length) {
        _raisedButton = '提交';
        //添加提交代码
        //_showScoreDialog控制按钮变成提交后，下一次点击再提交，并显示3秒的load框
        if (_showScoreDialog) {
          _getHttp();
          setState(() {
            _showLoading = true;
          });
          _scoreRequest().then((onValue) {
            setState(() {
              _showLoading = false;
            });
            if (_score == '') {
              showDialog(
                  context: context,
                  builder: (_) => new AlertDialog(
                          title: new Text("提示："),
                          content: new Text("获取分数失败"),
                          actions: <Widget>[
                            new FlatButton(
                              child: new Text("确定"),
                              onPressed: () {
                                Navigator.of(context).pop();
                              },
                            )
                          ]));
            }
          });
        }
        _showScoreDialog = true;
      }
    }
  }

  @override
  void initState() {
    super.initState();
    var ques = json.decode(questions);
    for (var i in ques) {
      var temp =
          Question(i['number'], i['question'], i['answers'], i['answer']);
      _questions.add(temp);
    }
  }

  @override
  Widget build(BuildContext context) {
    List<Widget> childrens = [];
    final _mainConatiner = Scaffold(
      appBar: AppBar(
        title: Text('入职考试'),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: EdgeInsets.all(16),
            child: Center(
                child: Text(
              "第${_index + 1}题：",
              style: TextStyle(fontSize: 18),
            )),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(10, 20, 18, 18),
            child: Text(
              _questions[_index].question,
              textAlign: TextAlign.left,
              style: TextStyle(fontSize: 14),
            ),
          ),
          Expanded(
            flex: 10,
            child: ListView.builder(
                itemCount: _questions[_index].answers.length,
                itemBuilder: (BuildContext context, i) {
                  return Row(
                    children: <Widget>[
                      Radio(
                          value: _questions[_index].answers[i].toString(),
                          groupValue: _newValue,
                          onChanged: (value) {
                            setState(() {
                              _newValue = value;
                              print('value:   *****************' + value);
                            });
                          }),
                      Text((i + 1).toString() +
                          '.   ' +
                          _questions[_index].answers[i].toString()),
                    ],
                  );
                }),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(0, 0, 0, 100),
            child: RaisedButton(child: Text(_raisedButton), onPressed: _submit),
          ),
        ],
      ),
    );
    final _loadingContainer = Container(
        constraints: BoxConstraints.expand(),
        color: Colors.black12,
        child: Center(
          child: Opacity(
            opacity: 0.9,
            child: SpinKitWave(
              color: Colors.red,
              size: 50.0,
            ),
          ),
        ));
    childrens.add(_mainConatiner);
    if (_showLoading) {
      childrens.add(_loadingContainer);
    }
    if (_score != '') {
      return AlertDialog(
        title: new Text('提示：'),
        content: new SingleChildScrollView(
          child: new ListBody(
            children: <Widget>[
              new Text('您本次的考核成绩为 $_score 分！'),
            ],
          ),
        ),
        actions: <Widget>[
          new FlatButton(
            child: new Text('确定'),
            onPressed: () {
              Navigator.pop(context, _score);
            },
          ),
        ],
      );
    } else {
      return Stack(
        children: childrens,
      );
    }
  }
}
