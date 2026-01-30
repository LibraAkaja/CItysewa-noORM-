import 'package:flutter/material.dart';

import 'package:citysewa_provider/api/api.dart' show AuthService;
import 'package:citysewa_provider/api/models.dart' show User;
import 'package:citysewa_provider/session_manager.dart' show SessionManager;

AuthService auth = AuthService();

class ProfileScreen extends StatefulWidget {
  ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  User? user;
  @override
  void initState() {
    super.initState();
    loadUser();
  }

  Future loadUser() async {
    final userLoaded = await SessionManager.getUser();
    if (userLoaded != null) {
      setState(() {
        user = userLoaded;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(automaticallyImplyLeading: false),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: ListView(
          children: [
            SizedBox(height: 10),
            Header(user),
            Visibility(
              visible: !user!.verified,
              child: Column(
                children: [SizedBox(height: 20), VerifyYourselfBanner()],
              ),
            ),
            SizedBox(height: 20),
            SettingsContainer(),
          ],
        ),
      ),
    );
  }
}

class Header extends StatefulWidget {
  final User? user;
  const Header(this.user, {super.key});

  @override
  State<Header> createState() => _HeaderState();
}

class _HeaderState extends State<Header> {
  String userName = "Guest";

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    userName = widget.user != null
        ? "${widget.user!.firstName} ${widget.user!.lastName}"
        : userName;
    return Container(
      padding: EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: Colors.white54,
        border: BoxBorder.all(color: Colors.grey),
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(30),
            blurRadius: 14,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          CircleAvatar(
            radius: 40,
            backgroundColor: Colors.white,
            backgroundImage: AssetImage('assets/images/test.png'),
          ),
          SizedBox(width: 20),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 5),
                Row(
                  spacing: 4,
                  children: [
                    Text(
                      userName,
                      style: TextStyle(fontSize: 16, color: Colors.black),
                    ),
                    Visibility(
                      visible: widget.user!.verified,
                      child: Icon(
                        Icons.check_circle_outline_rounded,
                        size: 16,
                        color: Colors.green,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
                Text(
                  "Carpenter",
                  style: TextStyle(fontSize: 14, color: Colors.black45),
                ),
                Visibility(
                  visible: !widget.user!.verified,
                  child: Text(
                    "Verification pending",
                    style: TextStyle(color: Colors.blue),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class VerifyYourselfBanner extends StatelessWidget {
  const VerifyYourselfBanner({super.key});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        Navigator.pushNamed(context, '/verify');
      },
      child: Container(
        padding: EdgeInsets.all(10),
        decoration: BoxDecoration(
          color: const Color.fromARGB(150, 98, 243, 173),
          border: Border.all(color: Colors.grey),
          borderRadius: BorderRadius.circular(15),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withAlpha(30),
              offset: Offset(0, 6),
              blurRadius: 6,
            ),
          ],
        ),
        child: RichText(
          text: const TextSpan(
            text: 'You are not verified yet. Please submit the ',
            style: TextStyle(fontSize: 15, color: Colors.blueGrey),
            children: [
              TextSpan(
                text: "verification form.",
                style: TextStyle(decoration: TextDecoration.underline),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsContainer extends StatelessWidget {
  const SettingsContainer({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(10),

      decoration: BoxDecoration(
        color: Colors.white38,
        border: Border.all(color: Colors.grey),
        borderRadius: BorderRadius.circular(15),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text("Settings", style: TextStyle(color: Colors.grey, fontSize: 16)),
          SettingTab("Account", "/account_settings"),
          SettingTab("Address", "/address_settings"),
          SettingTab("Profile", "/profile_settings"),
          SettingTab("Payment", "/payment_settings"),
        ],
      ),
    );
  }
}

class SettingTab extends StatelessWidget {
  final String name;
  final String path;
  const SettingTab(this.name, this.path, {super.key});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {},
      child: Padding(
        padding: EdgeInsets.symmetric(vertical: 2),
        child: Text(name, style: TextStyle(fontSize: 16)),
      ),
    );
  }
}
