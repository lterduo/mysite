import 'package:flutter/material.dart';
import '../constants.dart' show AppConstants;
import 'package:dio/dio.dart';
import 'dart:convert';

class Manage extends StatefulWidget {
  _ManageState createState() => _ManageState();
}

class _ManageState extends State<Manage> {
  var msg;
  int _counter = 0;
  void _getHttp() async {
    try {
      Response response;
      Dio dio = new Dio();
      response = await dio.get(AppConstants.ServiceId + "manage");
      msg = json.decode(response.data.toString());
      debugPrint('manage*************:' + msg.toString());
      setState(() {
        _counter = msg.length;
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
        body: Column(
      children: <Widget>[
        Expanded(
            child: ListView.builder(
                // itemCount: imgs.length,
                itemCount: _counter,
                itemBuilder: (BuildContext context, i) {
                  return Container(
                    child: Row(
                      children: <Widget>[
                        Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: <Widget>[
                            Text('账号：' + msg[i]['user_id'].toString()),
                            Text('姓名：' + msg[i]['name'].toString()),
                          ],
                        ),
                        Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: <Widget>[
                            Text('年龄：' + msg[i]['age'].toString()),
                            Text('分数：' + msg[i]['score'].toString()),
                          ],
                        ),
                        Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: <Widget>[
                            Text('角色：' + msg[i]['role'].toString()),
                            Text("入职时间：")
                          ],
                        )
                      ],
                    ),
                  );
                  // return Text(imgs[i]['img'].toString());
                })),
        Padding(
            padding: EdgeInsets.fromLTRB(0, 10, 0, 10),
            child: Row(
              children: <Widget>[
                Expanded(
                  child: Padding(
                    padding: EdgeInsets.all(10),
                    child: RaisedButton(
                      child: Text('新增员工'),
                      onPressed: () {},
                    ),
                  ),
                ),
                Expanded(
                  child: Padding(
                    padding: EdgeInsets.all(10),
                    child: RaisedButton(
                      child: Text('删除员工'),
                      onPressed: () {},
                    ),
                  ),
                )
              ],
            ))
      ],
    ));
  }
}
