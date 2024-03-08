import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Drag and Drop Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Drag and Drop Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<int> draggableNumbers = List.generate(10, (index) => index);
  int totalCount = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: draggableNumbers
                  .map(
                    (number) => Draggable<int>(
                      key: Key('draggable_$number'), // Add key for testing
                      data: number,
                      child: _buildNumberTile(number),
                      feedback: _buildNumberTile(number, isDragging: true),
                      childWhenDragging: Container(),
                    ),
                  )
                  .toList(),
            ),
            SizedBox(height: 20),
            DragTarget<int>(
              key: const Key('dragTarget'),
              onAccept: (value) {
                setState(() {
                  totalCount += value;
                });
                print("Dropped $value, Total Count: $totalCount");
              },
              builder: (context, accepted, rejected) {
                return Semantics(
                  label: 'dropBox',
                  child: Container(
                    key: const Key('dropBox'),
                    width: 100,
                    height: 100,
                    color: Colors.orange,
                    child: Center(
                      child: Text(
                        'Total: $totalCount',
                        style: TextStyle(fontSize: 18),
                      ),
                    ),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildNumberTile(int number, {bool isDragging = false}) {
    return Container(
      width: 50,
      height: 50,
      color: isDragging ? Colors.transparent : Colors.blue,
      child: Center(
        child: Text(
          '$number',
          style: TextStyle(
            fontSize: 18,
            color: isDragging ? Colors.black : Colors.white,
          ),
        ),
      ),
    );
  }
}
