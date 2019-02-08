import 'package:flutter/material.dart';
import 'pages/exam.dart';
import 'pages/manage.dart';
import 'pages/news.dart';

class Home extends StatefulWidget {
  final String userId;
  Home(String this.userId) {}
  _HomeState createState() => _HomeState(userId);
}

class _HomeState extends State<Home> {
  final String userId;
  _HomeState(String this.userId) {}

  PageController _pageController;
  int _index = 0;
  List<Widget> _pages = List();
  BottomNavigationBar _bottom;
  @override
  void initState() {
    super.initState();
    _pages..add(News())..add(Manage())..add(Exam());

    // _bottom = ;

    _pageController = PageController(initialPage: _index);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('郁陵岛  $userId'),
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
          items: [
            BottomNavigationBarItem(
                title: Text('岛内动态'),
                icon: Icon(IconData(0xe667, fontFamily: 'iconfont')),
                activeIcon: Icon(IconData(0xe664, fontFamily: 'iconfont')),
                ),
            BottomNavigationBarItem(
              title: Text('员工管理'),
              icon: Icon(IconData(0xe663, fontFamily: 'iconfont')),
              activeIcon: Icon(IconData(0xe72a, fontFamily: 'iconfont')),
            ),
            BottomNavigationBarItem(
              title: Text('入职考试'),
              icon: Icon(IconData(0xe660, fontFamily: 'iconfont')),
              activeIcon: Icon(IconData(0xe60d, fontFamily: 'iconfont')),
            ),
          ],
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
