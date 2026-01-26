import 'package:flutter/material.dart';

import 'package:citysewa_provider/screens/login_screen.dart' show LoginScreen;

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
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.red),
        fontFamily: 'Inter',
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
            backgroundColor: Colors.red,
            minimumSize: Size.fromHeight(50),
            textStyle: TextStyle(fontSize: 18),
          ),
        ),
      ),

      home: LoginScreen(),
    );
  }
}
