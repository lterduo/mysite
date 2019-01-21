import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  //构建一个容器
  Widget build(BuildContext context) {
    return new MaterialApp(
      theme: ThemeData(primaryColor: Colors.yellowAccent),
      title: 'Startup Name Generator',
      home: new RandomWords(),//定义子组件为有状态控件RandomWords类的实例
    );
  }
}

class RandomWords extends StatefulWidget{
  @override
  createState() => new RandomWordsState();
}

class RandomWordsState extends State<RandomWords>{
  @override
  // final _suggestions = <WordPair>[];
  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18.0);   //用于标识字符串的样式
  final _saved = Set<WordPair>();

  Widget build(BuildContext context) {
    return new Scaffold (
      appBar: new AppBar(
        title: new Text('Startup Name Generator'),
        actions: <Widget>[
          IconButton(icon: Icon(Icons.list),onPressed: _pushSaved,),
        ],
      ),
      body: _buildSuggestions(), 
    );
  }

  Widget _buildSuggestions() {
    return new ListView.builder(  //ListView(列表视图)是material.dart中的基础控件
      padding: const EdgeInsets.all(16.0),  //padding(内边距)是ListView的属性，配置其属性值
      //通过ListView自带的函数itemBuilder，向ListView中塞入行，变量 i 是从0开始计数的行号
      //此函数会自动循环并计数，咋结束的我也不知道，走着瞧咯
      itemBuilder: (context, i) {
        if (i.isOdd) return new Divider();//奇数行塞入分割线对象
        final index = i ~/ 2;  //当前行号除以2取整，得到的值就是_suggestions数组项索引号
        // 如果计算得到的数组项索引号超出了_suggestions数组的长度，那_suggestions就再生10个随机组合的字符串词组
        if (index >= _suggestions.length) {
          _suggestions.addAll(generateWordPairs().take(10));
        }
        print(Text('${_suggestions[index]}'));
        return _buildRow(_suggestions[index]);//把这个数据项塞入ListView中
      }
    );
  }

  //定义的_suggestions数组项属性
  Widget _buildRow(WordPair pair) {
    final alreadySaved = _saved.contains(pair);
    return new ListTile(
      title: new Text(
        pair.asPascalCase,  //使用驼峰样式
        style: _biggerFont,
      ),
      trailing: Icon(
        alreadySaved ? Icons.favorite : Icons.favorite_border,
        color: Colors.red,
      ),
      onTap: () {
        setState((){
          if (alreadySaved) {
            _saved.remove(pair);
          } else {
            _saved.add(pair);
          }
        });
      }
    );
  }
  //点击跳转 navigator用法
  void _pushSaved(){
    print('点我！');
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) {
          final tiles = _saved.map(
            (pair) {
              return Text('${pair.asPascalCase}');
            }
          );
          return Scaffold(
            appBar: AppBar(title: Text('收藏列表'),), 
            body: ListView(
              children: tiles.toList(),
            )
          );
        }
      )
    );
  }
}