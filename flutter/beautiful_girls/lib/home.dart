import 'package:flutter/material.dart';
import 'pages/exam.dart';
import 'pages/manage.dart';
import 'pages/news.dart';
import 'pages/customer.dart';
import 'pages/joomla.dart';
import 'dart:convert';

class Home extends StatefulWidget {
  final String userInfo;  //传入的是整个users表信息
  Home(this.userInfo);
  _HomeState createState() => _HomeState(userInfo);
}

class _HomeState extends State<Home> {
  final String userInfo;
  _HomeState(this.userInfo);

  var info;
  PageController _pageController;
  int _index = 0;
  List<Widget> _pages = List();
  List<BottomNavigationBarItem> _bottom;
  String userName;
  @override
  void initState() {
    super.initState();
    info = json.decode(userInfo); //转换成map使用用户的具体信息
    userName = info['name'];

    _pages..add(Customer())..add(News())..add(Exam(info['user_id']))..add(Joomla());

    _bottom = [
      BottomNavigationBarItem(
        title: Text('客户管理'),
        icon: Icon(IconData(0xe667, fontFamily: 'iconfont')),
        activeIcon: Icon(IconData(0xe664, fontFamily: 'iconfont')),
      ),
      BottomNavigationBarItem(
        title: Text('岛内动态'),
        icon: Icon(IconData(0xe667, fontFamily: 'iconfont')),
        activeIcon: Icon(IconData(0xe664, fontFamily: 'iconfont')),
      ),
      BottomNavigationBarItem(
        title: Text('入职考试'),
        icon: Icon(IconData(0xe660, fontFamily: 'iconfont')),
        activeIcon: Icon(IconData(0xe60d, fontFamily: 'iconfont')),
      ),
      BottomNavigationBarItem(
        title: Text('网页测试'),
        icon: Icon(IconData(0xe667, fontFamily: 'iconfont')),
        activeIcon: Icon(IconData(0xe664, fontFamily: 'iconfont')),
      ),
    ];
    //如果是管理角色，加上员工管理
    if (info['role'] == 'manager') {
      _pages..add(Manage());
      _bottom
        ..add(BottomNavigationBarItem(
          title: Text('员工管理'),
          icon: Icon(IconData(0xe663, fontFamily: 'iconfont')),
          activeIcon: Icon(IconData(0xe72a, fontFamily: 'iconfont')),
        ));
    }

    _pageController = PageController(initialPage: _index);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('郁陵岛  $userName'),
          actions: <Widget>[
            IconButton(
              icon: Icon(IconData(0xe616, fontFamily: 'iconfont')),
              onPressed: (){},)
          ],
        ),
        body: PageView.builder(
          itemBuilder: (BuildContext contenxt, int index) {
            return _pages[index];
          },
          controller: _pageController,
          itemCount: _pages.length,
          onPageChanged: (index) {
            setState(() {
              _index = index;
            });
          },
        ),
        bottomNavigationBar: BottomNavigationBar(
          items: _bottom,
          currentIndex: _index,
          type: BottomNavigationBarType.fixed,
          onTap: (index) {
            setState(() {
              _index = index;
              _pageController.animateToPage(_index,
                  duration: Duration(milliseconds: 200),
                  curve: Curves.bounceIn);
            });
          },
        ));
  }
}
