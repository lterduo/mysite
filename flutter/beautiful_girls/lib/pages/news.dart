import 'package:flutter/material.dart';

class News extends StatefulWidget {
  _NewsState createState() => _NewsState();
}

class _NewsState extends State<News> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text('News')
      )
    );
  }
}