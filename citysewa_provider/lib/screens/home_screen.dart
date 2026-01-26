import "package:flutter/material.dart";
import "package:shared_preferences/shared_preferences.dart"
    show SharedPreferences;

class HomeScreen extends StatefulWidget {
  HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Text("Hello Citysewa"));
  }
}
