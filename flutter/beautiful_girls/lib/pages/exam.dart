import 'package:flutter/material.dart';
import 'dart:convert';

class Question {
  final String number;
  final String question;
  final List answers;
  final String answer;
  Question(this.number, this.question, this.answers, this.answer);
}

class Exam extends StatefulWidget {
  _ExamState createState() => _ExamState();
}

class _ExamState extends State<Exam> {
  List _result = [];
  int _index = 0;
  List<Question> _questions = List();
  static String que = '''
    [{"number": "1", "question": "1 + 1 = ?", "answers": ["2", "3", "4"], "answer": "2"},
    {"number": "2", "question": "1 + 2 = ?", "answers": ["2", "3", "4"], "answer": "3"},
    {"number": "3", "question": "2 + 2 = ?", "answers": ["2", "3", "4"], "answer": "4"}]
  ''';
  List ques = json.decode(que);
  @override
  void initState() {
    super.initState();
    for (var i in ques) {
      var temp =
          Question(i['number'], i['question'], i['answers'], i['answer']);
      _questions.add(temp);
    }
  }

  String _newValue = "";
  bool _offstage = true;
  String _raisedButton = '下一题';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
                              print('*****************' + value);
                            });
                          }),
                      Text((i + 1).toString() +
                          '.   ' +
                          _questions[_index].answers[i].toString()),
                    ],
                  );
                }),
          ),
          RaisedButton(
            child: Text(_raisedButton),
            onPressed: () {
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
                setState(() {
                  if (_result.length < _questions.length) {
                    _result.add({_index: _newValue});
                  }
                  debugPrint(_result.toString());
                  if (_index + 1 < _questions.length) {
                    _index = _index + 1;
                    _newValue = '';
                  }
                  if (_index + 1 == _questions.length) {
                    _offstage = false;
                    _raisedButton = '提交';
                    //添加提交代码
                  }
                });
              }
            },
          ),
          Offstage(
            offstage: _offstage,
            child: Text('您考核的成绩是：100 分！'),)
        ],
      ),
      // floatingActionButton: Offstage(
      //   offstage: _offstage,
      //   child:
      // FloatingActionButton(
      //   child: Text('提交'),
      //   onPressed: () {},
      // ),),
    );
  }
}
