import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'dart:convert';

class BeautifulGirls extends StatefulWidget {
  _BeautifulGirlsState createState() => _BeautifulGirlsState();
}

class _BeautifulGirlsState extends State<BeautifulGirls> {
  //请求网络数据
  final Dio dio = Dio();
  List imgs = [];
  int _itemCount = 0;
  void getHttp() async {
    try {
      Response response = await dio.get('http://192.168.1.124:8000/vue_home');
      //非常重要，避免渲染时获得空数据而报错。我写的这段没效果，而是在imgs加了await
      if (!mounted) return;  
      var msg = response.data.toString();
      imgs =  await json.decode(msg);
      setState(() {
        _itemCount = imgs.length;
      });
      _itemCount = imgs.length;
    } catch (e) {
      return print(e);
    }
  }
  

  void initState() {
    super.initState();

    getHttp();

    // _pages = [
    //   ListView.builder(
    //       itemCount: 20,
    //       // itemExtent: 20.0, //强制高度为50.0
    //       itemBuilder: (BuildContext context, int index) {
    //         // return Image.network(tempString,width:100);
    //         return Text('haha$index');
    //       }),
    //   Container(
    //     color: Colors.black,
    //   ),
    //   Container(
    //     color: Colors.blue,
    //   ),
    //   Container(
    //     color: Colors.pink,
    //   ),
    // ];
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: '老板福利',
        theme: new ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: Scaffold(
            appBar: AppBar(
              title: Text('老板福利'),
            ),
            body: Container(
                child: ListView.builder(
                    // itemCount: imgs.length,
                    itemCount: _itemCount,
                    itemBuilder: (BuildContext context, i) {
                      return Image.network(imgs[i]['img'].toString());
                      // return Text(imgs[i]['img'].toString());
                    }))

            // body: Column(
            //   children: <Widget>[
            //     Expanded(
            //       child: PageView.builder(
            //         itemBuilder: (BuildContext contenxt, int index) {
            //           return _pages[index];
            //         },
            //         controller: _pageController,
            //         itemCount: _pages.length,
            //         onPageChanged: (i) {
            //           //和图标联动
            //           setState(() {
            //             _currentIndex = i;
            //           });
            //         },
            //       ),
            //     ),
            //     Container(
            //       color: Colors.red,
            //       height: 80,
            //     ),
            //   ],
            // ),
            ));
  }
}
