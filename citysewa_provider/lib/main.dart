import 'package:flutter/material.dart';

import 'package:citysewa_provider/screens/login_screen.dart' show LoginScreen;
import 'package:citysewa_provider/screens/signup_screen.dart' show SignupScreen;
import 'package:citysewa_provider/screens/home_screen.dart' show HomeScreen;
import 'package:citysewa_provider/screens/profile_screen.dart'
    show ProfileScreen;

void main() {
  runApp(RootApp());
}

class RootApp extends StatelessWidget {
  const RootApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Citysewa Provider',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange),
        fontFamily: 'Inter',
        textTheme: ThemeData.light().textTheme.apply(fontFamily: 'Inter'),
        appBarTheme: AppBarThemeData(
          backgroundColor: Colors.deepOrange,
          centerTitle: true,
          toolbarHeight: 5,
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
        snackBarTheme: SnackBarThemeData(
          backgroundColor: Colors.redAccent,
          contentTextStyle: TextStyle(fontSize: 14, color: Colors.white),
          behavior: SnackBarBehavior.floating,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => LoginScreen(),
        '/register': (context) => SignupScreen(),
        '/home': (context) => HomeScreen(),
        '/profile': (context) => ProfileScreen(),
      },
    );
  }
}
