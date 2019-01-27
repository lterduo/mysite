import 'package:flutter/material.dart';
import '../constants.dart' show Constants, AppColors;

//定义一个地步导航按钮的数据结构
class NavigationIconView {
  // final String _title;
  // final Widget _icon;
  // final Widget _activeIcon;
  final BottomNavigationBarItem item;
  NavigationIconView(
      {Key key, String title, IconData icon, IconData activeIcon})
      :
        // _title = title,
        // _icon = icon,
        // _activeIcon = activeIcon,
        item = new BottomNavigationBarItem(
          title: Text(title,
              style: TextStyle(
                fontSize: 14,
                color: Color(AppColors.TabIconActive),
              )),
          icon: Icon(
            icon,
            color: Color(AppColors.TabIconNormal),
          ),
          activeIcon: Icon(
            activeIcon,
            color: Color(AppColors.TabIconActive),
          ),
          backgroundColor: Colors.blue,
        );
}

class HomeScreen extends StatefulWidget {
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  //控制pageview
  PageController _pageController;
  List<Widget> _pages;
  List<NavigationIconView> _navigationViews;
  //第几个图标
  var _currentIndex = 0;
  void initState() {
    super.initState();

    //图标都使用iconfont
    _navigationViews = <NavigationIconView>[
      NavigationIconView(
        title: '微信',
        icon: IconData(0xe64f, fontFamily: Constants.IconFontFamily),
        activeIcon: IconData(0xe620, fontFamily: Constants.IconFontFamily),
      ),
      NavigationIconView(
        title: '通讯录',
        icon: IconData(0xe6c9, fontFamily: Constants.IconFontFamily),
        activeIcon: IconData(0xe64d, fontFamily: Constants.IconFontFamily),
      ),
      NavigationIconView(
        title: '发现',
        icon: IconData(0xe629, fontFamily: Constants.IconFontFamily),
        activeIcon: IconData(0xe602, fontFamily: Constants.IconFontFamily),
      ),
      NavigationIconView(
        title: '我',
        icon: IconData(0xe67d, fontFamily: Constants.IconFontFamily),
        activeIcon: IconData(0xe616, fontFamily: Constants.IconFontFamily),
      ),
    ];
    _pageController = PageController(initialPage: _currentIndex);
    //初始化内容页
    _pages = [
      Container(
        color: Colors.white,
      ),
      Container(
        color: Colors.black,
      ),
      Container(
        color: Colors.blue,
      ),
      Container(
        color: Colors.pink,
      ),
    ];
  }

  @override
  Widget build(BuildContext context) {
    //使用底部导航栏

    final BottomNavigationBar _botNavBar = BottomNavigationBar(
      items: _navigationViews.map((NavigationIconView view) {
        return view.item;
      }).toList(),
      currentIndex: _currentIndex,
      type: BottomNavigationBarType.fixed,
      onTap: (int index) {
        setState(() {
          _currentIndex = index;
          //控制pages
          _pageController.animateToPage(_currentIndex,
              duration: Duration(milliseconds: 200), curve: Curves.bounceIn);
        });
        print('点击了$index');
      },
    );
    return Scaffold(
      appBar: AppBar(
        title: Text(
          '我的微信',
        ),
        //appBar上面添加的内容，比如搜索等
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.search),
            onPressed: () {
              print('search');
            },
          ),
          Container(
            width: 20,
          ),
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () {
              print('add');
            },
          ),
        ],
      ),
      body: PageView.builder(
        itemBuilder: (BuildContext contenxt, int index) {
          return _pages[index];
        },
        controller: _pageController,
        itemCount: _pages.length,
        onPageChanged: (i) {
          //和图标联动
          setState(() {
            _currentIndex = i;
          });
        },
      ),
      bottomNavigationBar: _botNavBar,
    );
  }
}
