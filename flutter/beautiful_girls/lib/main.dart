import 'package:flutter/material.dart';
// import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:flutter/rendering.dart';
import 'beautiful_girls.dart';
import 'home.dart';

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

  Future _loginRequest() async {
    return Future.delayed(Duration(seconds: 0), () {});
  }

  void _toggleSubmit() {
    if (_formKey.currentState.validate()) {
      setState(() {
        _showLoading = true;
      });

      _loginRequest().then((onValue) {
        setState(() {
          _showLoading = false;
        });
        if (_userNameTextController.text == 'a' &&
            _passwordTextController.text == 'a') {
        // if (true) {
          Navigator.pushAndRemoveUntil(context,
              MaterialPageRoute(builder: (context) => Home(_userNameTextController.text))
              , (route) => route == null);
        } else {
          String alertText = '请不要盗用老板的账号！';
          showDialog<Null>(
            context: context,
            barrierDismissible: false,
            builder: (BuildContext context) {
              return new AlertDialog(
                title: new Text('警告：'),
                content: new SingleChildScrollView(
                  child: new ListBody(
                    children: <Widget>[
                      new Text(alertText),
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
          ).then((val) {
            print(val);
          });
        }
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
                      hintText: '报上名来', prefixIcon: Icon(Icons.person)),
                  validator: (value) {
                    if (value.isEmpty) {
                      return '请输入您的姓名';
                    }
                  },
                  controller: _userNameTextController,
                ),
                TextFormField(
                  decoration: InputDecoration(
                      hintText: '说出暗号', prefixIcon: Icon(Icons.lock)),
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
  }
}
