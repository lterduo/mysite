import 'package:flutter/foundation.dart';
import 'package:web_socket_channel/io.dart';
import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import '../constants.dart' show AppConstants;

class Customer extends StatefulWidget {
  final Widget child;

  Customer({Key key, this.child}) : super(key: key);

  _CustomerState createState() => _CustomerState();
}

class _CustomerState extends State<Customer> {
  var channel = IOWebSocketChannel.connect(AppConstants.ServiceIdWS + 'customer');

  TextEditingController _controller = new TextEditingController();
  String msg = '';
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          new Form(
            child: new TextFormField(
              controller: _controller,
              decoration: new InputDecoration(labelText: 'Send a message'),
            ),
          ),
          StreamBuilder(
            stream: channel.stream,
            builder: (context, snapshot) {
              return Expanded(
                child: ListView.builder(
                  itemCount: 10,
                  itemBuilder: (BuildContext context, int index) {
                  return Text(snapshot.hasData ? '${snapshot.data}' : '');
                 },
                ),
              );
            },
          )
        ],
      ),

      floatingActionButton: new FloatingActionButton(
        onPressed: _sendMessage,
        tooltip: 'Send message',
        child: new Icon(Icons.send),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  void _sendMessage() {
    if (_controller.text.isNotEmpty) {
      setState(() {
        channel.sink.add(_controller.text);
      });
    }
  }

  @override
  void dispose() {
    channel.sink.close();
    super.dispose();
  }
}
