import 'package:flutter/material.dart';

import 'package:citysewa_provider/screens/login_screen.dart' show LoginScreen;
import 'package:citysewa_provider/screens/home_screen.dart' show HomeScreen;

void main() {
  runApp(RootApp());
}

class RootApp extends StatelessWidget {
  const RootApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange),
        fontFamily: 'Inter',
        textTheme: ThemeData.light().textTheme.apply(fontFamily: 'Inter'),
        appBarTheme: AppBarThemeData(
          backgroundColor: Colors.deepOrange,
          centerTitle: true,
          toolbarHeight: kToolbarHeight,
        ),
        inputDecorationTheme: InputDecorationTheme(
          fillColor: Color(0xfffffefe),
          hoverColor: Color(0xfffffefe),
          filled: true,
          enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(width: 1, color: Colors.black45),
            borderRadius: BorderRadius.circular(10),
          ),
          focusColor: Colors.red,
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(width: 1.5, color: Colors.black),
            borderRadius: BorderRadius.circular(10),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(20),
            ),
            foregroundColor: Colors.white,
            backgroundColor: Colors.deepOrange,
            minimumSize: Size.fromHeight(50),
            textStyle: TextStyle(fontSize: 18),
          ),
        ),
        snackBarTheme: SnackBarThemeData(backgroundColor: Colors.deepOrange),
      ),
      home: HomeScreen(),
    );
  }
}
