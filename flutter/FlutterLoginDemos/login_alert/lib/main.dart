import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:flutter/rendering.dart';
import 'package:dio/dio.dart';

void main() {
  debugPaintSizeEnabled = false;
  runApp(new LoginAlertDemoApp());
}

class LoginAlertDemoApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
        title: 'Login Alert',
        theme: new ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: Scaffold(
          appBar: AppBar(
            title: Text('Login Alert'),
          ),
          body: new LoginHomePage(),
        ));
  }
}

class LoginHomePage extends StatefulWidget {
  @override
  _LoginHomePageState createState() {
    // TODO: implement createState
    return new _LoginHomePageState();
  }
}

class _LoginHomePageState extends State<LoginHomePage> {
  final _formKey = GlobalKey<FormState>();
  final _userNameTextController = TextEditingController();
  final _passwordTextController = TextEditingController();
  bool _showLoading = false;
  String userName = '';
  String logSuccess = '';

  void _getHttp() async {
    try {
      Response response;
      Dio dio = new Dio();
      // response = await dio.get("/test?id=12&name=wendu");
      // response = await dio.get("http://47.104.242.85:8000/get_user", data: {
      response = await dio.get("http://192.168.1.102:8000/get_user", data: {
        "user_id": _userNameTextController.text,
        "password": _passwordTextController.text
      });
      var msg = response.data.toString();
      debugPrint('msg:           ' + msg);
      var msgs = msg.split('?');
      debugPrint('msgs:           ' + msgs.toString());
      setState(() {
        userName = msgs[0];
        logSuccess = msgs[1];
      });
    } catch (e) {
      print(e);
    }
  }

  Future _loginRequest() async {
    return Future.delayed(Duration(seconds: 3), () {
      //do nothing
      print('login success');
    });
  }

  void _toggleSubmit() {
    if (_formKey.currentState.validate()) {
      setState(() {
        _showLoading = true;
      });
      _getHttp();
      _loginRequest().then((onValue) {
        setState(() {
          _showLoading = false;
        });
        showDialog(
            context: context,
            builder: (context) {
              String alertText = 'login success!' +
                  ' \nuserName:' +
                  _userNameTextController.text +
                  '\npassWord:' +
                  _passwordTextController.text;
              return AlertDialog(
                content: Text(alertText),
              );
            });
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    List<Widget> childrens = [];
    final _mainConatiner = Container(
      padding: EdgeInsets.all(10.0),
      child: Form(
        key: _formKey,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Image.asset(
              'images/lake.jpg',
              height: 180.0,
              fit: BoxFit.fitHeight,
            ),
            Padding(
              padding: EdgeInsets.only(top: 50.0),
            ),
            TextFormField(
              decoration: InputDecoration(hintText: 'user name'),
              validator: (value) {
                if (value.isEmpty) {
                  return 'Please enter user name';
                }
              },
              controller: _userNameTextController,
            ),
            TextFormField(
              decoration: InputDecoration(hintText: 'password'),
              validator: (value) {
                if (value.isEmpty) {
                  return 'Please enter password';
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
                  'Submit',
                  style: TextStyle(color: Colors.white, fontSize: 20.0),
                ),
                color: Colors.blue,
              ),
            )
          ],
        ),
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
    if (logSuccess == 'yes') {
      
    }
    return Stack(
      children: childrens,
    );
  }
}
