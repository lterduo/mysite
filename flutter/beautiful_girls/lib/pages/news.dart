import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'dart:convert';
import '../constants.dart' show AppConstants;

class News extends StatefulWidget {
  _NewsState createState() => _NewsState();
}

class _NewsState extends State<News> {
  final Dio dio = Dio();
  List imgs = [];
  int _itemCount = 0;
  void getHttp() async {
    try {
      Response response = await dio.get(AppConstants.ServiceId + 'news');
      //非常重要，避免渲染时获得空数据而报错。我写的这段没效果，而是在imgs加了await
      if (!mounted) return;
      var msg = response.data.toString();
      imgs = json.decode(msg);
      setState(() {
        _itemCount = imgs.length;
      });
    } catch (e) {
      return print(e);
    }
  }

  void initState() {
    super.initState();
    getHttp();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        child: ListView.builder(
            // itemCount: imgs.length,
            itemCount: _itemCount,
            itemBuilder: (BuildContext context, i) {
              return Container(
                decoration:BoxDecoration(
                  border: Border(
                    bottom: BorderSide(
                      color: Colors.black,
                      width: 2
                    )
                  )
                ),
                child: Image.network(imgs[i]['img'].toString()),
              );
              // return Text(imgs[i]['img'].toString());
            }));
  }
}
