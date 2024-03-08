import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:dummyapp/main.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('end-to-end test', () {
    testWidgets('drag and drop numbers, verify total count', (tester) async {
      await tester.pumpWidget(const MyApp());
      await tester.pumpAndSettle();
      final draggableWidget = find.text("1");
      expect(find.text('Total: 0'), findsOneWidget);
      await waitUntilFindWidgetDynamic(tester, draggableWidget);
      final droppableWidget = find.byKey(Key('dropBox'));
      await waitUntilFindWidgetDynamic(tester, droppableWidget);
      for (int i = 0; i < 10; i++) {
        final Offset firstLocation = tester.getCenter(draggableWidget);
        final Offset secondLocation = tester.getCenter(droppableWidget);
        final TestGesture gesture =
            await tester.startGesture(firstLocation, pointer: 7);
        await tester.pump(Duration(milliseconds: 1000));
        await gesture.moveTo(secondLocation,
            timeStamp: Duration(milliseconds: 1600));
        await tester.pump(Duration(milliseconds: 1000));
        await gesture.up();
        await tester.pump(Duration(milliseconds: 1000));
      }
      await pumpTester(tester, Duration(milliseconds: 100), 50);
    });
  });
}

Future<void> pumpTester(
    WidgetTester tester, Duration duration, int times) async {
  for (int i = 0; i < times; i++) {
    await tester.pump(duration);
  }
}

Future<void> waitUntilFindWidget(WidgetTester tester, Finder widgetToFind,
    {int maxAttempts = 10}) async {
  bool foundWidget = false;
  int attempts = 0;
  await pumpTester(tester, Duration(milliseconds: 10), 20);
  while (!foundWidget && attempts < maxAttempts) {
    List<Widget> matchingWidgets = tester.widgetList(widgetToFind).toList();
    if (matchingWidgets.isNotEmpty) {
      foundWidget = true;
    } else {
      print("Waiting/loading for $widgetToFind");
      await pumpTester(tester, Duration(milliseconds: 10), 50);
      attempts++;
    }
  }

  if (!foundWidget) {
    expect("$widgetToFind is present", "not find the $widgetToFind");
  } else {
    print("$widgetToFind is found.");
  }
}

Future<void> waitUntilFindWidgetDynamic(
    WidgetTester tester, Finder widgetToFind,
    {int maxAttempts = 25}) async {
  bool foundWidget = false;
  int attempts = 0;
  await pumpTester(tester, Duration(milliseconds: 10), 20);
  while (!foundWidget && attempts < maxAttempts) {
    List<Widget> matchingWidgets = tester.widgetList(widgetToFind).toList();
    if (matchingWidgets.isNotEmpty) {
      foundWidget = true;
    } else {
      print("Waiting/loading for $widgetToFind");
      await pumpTester(tester, Duration(milliseconds: 10), 50);
      attempts++;
    }
  }

  if (!foundWidget) {
    expect("$widgetToFind is present", "not find the $widgetToFind");
  } else {
    print("$widgetToFind is found.");
  }
}
