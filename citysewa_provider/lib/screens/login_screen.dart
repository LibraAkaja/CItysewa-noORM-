import "package:flutter/material.dart";

import "package:citysewa_provider/widgets/widgets.dart" show AppLogo;
import 'package:citysewa_provider/screens/signup_screen.dart' show SignupScreen;
import 'package:citysewa_provider/screens/home_screen.dart' show HomeScreen;
import 'package:citysewa_provider/api/api.dart' show AuthService;

AuthService auth = AuthService();

class LoginScreen extends StatefulWidget {
  LoginScreen({super.key});

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xfffbf0f9),
      body: Center(
        child: ConstrainedBox(
          constraints: BoxConstraints(maxWidth: 400),
          child: Padding(
            padding: EdgeInsets.all(10),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                AppLogo(size: 50),
                SizedBox(height: 10),
                WelcomeText(),
                SizedBox(height: 20),
                LoginForm(),
                SizedBox(height: 20),
                GoToSignup(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class WelcomeText extends StatelessWidget {
  const WelcomeText({super.key});
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      child: Center(
        child: Column(
          children: [
            Text("Welcome Back", style: TextStyle(fontSize: 16)),
            Text(
              "Login to continue",
              style: TextStyle(fontSize: 14, color: Color(0xff6e6a6a)),
            ),
          ],
        ),
      ),
    );
  }
}

class LoginForm extends StatefulWidget {
  const LoginForm({super.key});
  _LoginFormState createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  bool isLoading = false;
  @override
  void initState() {
    super.initState();
  }

  void login(String email, String password) async {
    setState(() {
      isLoading = true;
    });
    try {
      final result = await auth.login(email, password);
      print("result: $result");
      if (result != null) {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => HomeScreen()),
        );
      }
    } catch (e) {
      print("Error: $e");
    }
    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final emailController = TextEditingController();
    final passController = TextEditingController();
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextField(
            controller: emailController,
            keyboardType: TextInputType.emailAddress,
            decoration: InputDecoration(
              hintText: "Email",
              prefixIcon: Icon(Icons.email_outlined),
            ),
          ),
          SizedBox(height: 20),
          TextField(
            controller: passController,
            obscureText: true,
            decoration: InputDecoration(
              hintText: "Password",

              prefixIcon: Icon(Icons.lock_outline),
            ),
          ),
          Container(
            margin: EdgeInsets.symmetric(vertical: 5),
            alignment: Alignment.bottomRight,
            child: InkWell(
              onTap: () {},
              child: const Text(
                "Forgot password?",
                style: TextStyle(color: Colors.red, fontSize: 14),
              ),
            ),
          ),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(),
              child: isLoading
                  ? CircularProgressIndicator(color: Colors.white)
                  : const Text(
                      "Login",
                      style: TextStyle(color: Colors.white, fontSize: 18),
                    ),
              onPressed: () {
                final email = emailController.text.toString().trim();
                final password = passController.text.toString().trim();
                if (email.isNotEmpty && password.isNotEmpty) {
                  login(
                    emailController.text.toString(),
                    passController.text.toString(),
                  );
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      backgroundColor: Colors.red,
                      content: Center(
                        child: Text(
                          "Ensure you entered correct credentials.",
                          style: TextStyle(
                            fontSize: 16,
                            fontStyle: FontStyle.italic,
                          ),
                        ),
                      ),
                    ),
                  );
                }
              },
            ),
          ),
        ],
      ),
    );
  }
}

class GoToSignup extends StatelessWidget {
  GoToSignup({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text("Dont`t have an account? ", style: TextStyle(fontSize: 16)),
        InkWell(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SignupScreen()),
            );
          },
          child: Text(
            "Sign Up",
            style: TextStyle(color: Colors.red, fontSize: 16),
          ),
        ),
      ],
    );
  }
}
