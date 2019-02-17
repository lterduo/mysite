import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:flutter/rendering.dart';
import 'home.dart';
import 'package:dio/dio.dart';
import 'dart:convert';
import './constants.dart' show AppConstants;

void main() {
  debugPaintSizeEnabled = false;
  runApp(new LoginAlertDemoApp());
}

class LoginAlertDemoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
        title: '郁陵岛员工管理系统',
        theme: new ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: LoginHomePage());
  }
}

class LoginHomePage extends StatefulWidget {
  @override
  _LoginHomePageState createState() {
    return new _LoginHomePageState();
  }
}

class _LoginHomePageState extends State<LoginHomePage> {
  final _formKey = GlobalKey<FormState>();
  final _userNameTextController = TextEditingController();
  final _passwordTextController = TextEditingController();
  bool _showLoading = false;
  String userId = '', userName = '';
  String logSuccess = '';
  var msg, msgs;

  Future _loginRequest() async {
    return Future.delayed(Duration(seconds: 3), () {});
  }

  void _getHttp() async {
    try {
      Response response;
      Dio dio = new Dio();
      response = await dio.get(AppConstants.ServiceId + "auth", data: {
        "user_id": _userNameTextController.text,
        "password": _passwordTextController.text
      });
      msg = response.data.toString();
      msgs = json.decode(msg);
      setState(() {
        logSuccess = msgs['user_id'];
      });
    } catch (e) {
      print(e);
    }
  }

  void _toggleSubmit() {
    _getHttp();
    if (_formKey.currentState.validate()) {
      setState(() {
        _showLoading = true;
      });
      _loginRequest().then((onValue) {
        setState(() {
          _showLoading = false;
        });
        if (logSuccess == '') {
          showDialog(
              context: context,
              builder: (_) => new AlertDialog(
                      title: new Text("提示："),
                      content: new Text("验证失败！"),
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
  }

//根据logSuccess来return不同页面
  @override
  Widget build(BuildContext context) {
    List<Widget> childrens = [];
    final _mainConatiner = Scaffold(
        appBar: AppBar(
          title: Text('郁陵岛'),
        ),
        body: Container(
          padding: EdgeInsets.all(10.0),
          child: Form(
            key: _formKey,
            child: ListView(
              children: <Widget>[
                Image.asset(
                  'images/kaorou.jpg',
                  height: 180.0,
                  fit: BoxFit.fitHeight,
                ),
                Padding(
                  padding: EdgeInsets.only(top: 50.0),
                ),
                TextFormField(
                  decoration: InputDecoration(
                      hintText: '账号', prefixIcon: Icon(Icons.person)),
                  validator: (value) {
                    if (value.isEmpty) {
                      return '请输入您的姓名';
                    }
                  },
                  controller: _userNameTextController,
                ),
                TextFormField(
                  decoration: InputDecoration(
                      hintText: '密码', prefixIcon: Icon(Icons.lock)),
                  validator: (value) {
                    if (value.isEmpty) {
                      return '请输入您的密码';
                    }
                  },
                  controller: _passwordTextController,
                  obscureText: true,
                ),
                Padding(
                  padding: EdgeInsets.only(top: 20.0),
                ),
                SizedBox(
                  width: double.infinity,
                  height: 50.0,
                  child: RaisedButton(
                    onPressed: _toggleSubmit,
                    child: Text(
                      '登录',
                      style: TextStyle(color: Colors.white, fontSize: 20.0),
                    ),
                    color: Colors.blue,
                  ),
                )
              ],
            ),
          ),
        ));
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
    if (logSuccess != '') {
      return Home(msg);
    } else {
      return Stack(
        children: childrens,
      );
    }
  }
}
