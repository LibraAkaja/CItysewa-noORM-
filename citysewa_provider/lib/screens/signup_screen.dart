import "package:flutter/material.dart";

import "package:citysewa_provider/widgets/widgets.dart" show AppLogo;
import "package:citysewa_provider/api/api.dart" show AuthService;

AuthService auth = AuthService();

class SignupScreen extends StatefulWidget {
  const SignupScreen({super.key});

  @override
  _SignupScreenState createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xfffbf0f9),
      body: Center(
        child: ConstrainedBox(
          constraints: BoxConstraints(maxWidth: 400),
          child: Padding(
            padding: EdgeInsets.all(20),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                AppLogo(size: 50),
                SizedBox(height: 10),
                WelcomeText(),
                SizedBox(height: 20),
                SignupForm(),
                const SizedBox(height: 20),
                GoToLogin(),
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
            Text("Become a part of the family", style: TextStyle(fontSize: 16)),
            Text(
              "Local Service, Made Simple",
              style: TextStyle(fontSize: 14, color: Color(0xff6e6a6a)),
            ),
          ],
        ),
      ),
    );
  }
}

class SignupForm extends StatefulWidget {
  const SignupForm({super.key});
  _SignupFormState createState() => _SignupFormState();
}

class _SignupFormState extends State<SignupForm> {
  bool isLoading = false;
  @override
  void initState() {
    super.initState();
  }

  void signUp(
    String fisrtName,
    String lastName,
    String email,
    String password,
  ) async {
    setState(() => isLoading = true);

    try {
      final result = await auth.register(fisrtName, lastName, email, password);
      print("result: $result");
      if (result != null) {
        Navigator.pop(context);
      }
    } catch (e) {
      print(e);
    }
    setState(() => isLoading = false);
  }

  @override
  Widget build(BuildContext context) {
    TextEditingController emailController = TextEditingController();
    TextEditingController passController = TextEditingController();
    TextEditingController firstNameController = TextEditingController();
    TextEditingController lastNameController = TextEditingController();
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          TextField(
            controller: firstNameController,
            keyboardType: TextInputType.name,
            decoration: InputDecoration(
              hintText: "First name",
              prefixIcon: Icon(Icons.abc_rounded),
            ),
          ),

          SizedBox(height: 10),
          TextField(
            controller: lastNameController,
            keyboardType: TextInputType.name,
            decoration: InputDecoration(
              hintText: "Last name",
              prefixIcon: Icon(Icons.abc),
            ),
          ),

          const SizedBox(height: 10),
          TextField(
            controller: emailController,
            keyboardType: TextInputType.emailAddress,
            decoration: InputDecoration(
              hintText: "Email",
              prefixIcon: Icon(Icons.email_outlined),
            ),
          ),

          SizedBox(height: 10),
          TextField(
            controller: passController,
            obscureText: true,
            decoration: InputDecoration(
              hintText: "Password",
              prefixIcon: Icon(Icons.lock_outline),
            ),
          ),

          const SizedBox(height: 10),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              child: isLoading
                  ? CircularProgressIndicator(color: Colors.white)
                  : Text("Register"),
              onPressed: () {
                final String firstName = firstNameController.text
                    .toString()
                    .trim();
                final String lastName = lastNameController.text
                    .toString()
                    .trim();
                final String email = emailController.text.toString().trim();
                final String password = passController.text.toString().trim();
                if (email.isNotEmpty &&
                    password.isNotEmpty &&
                    firstName.isNotEmpty &&
                    lastName.isNotEmpty) {
                  signUp(firstName, lastName, email, password);
                } else {
                  String msg = "Please ensure that you filed form correctly.";
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      backgroundColor: Colors.red,
                      content: Center(
                        child: Text(
                          msg,
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

class GoToLogin extends StatelessWidget {
  GoToLogin({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text("Already have an account? ", style: TextStyle(fontSize: 16)),
        InkWell(
          onTap: () {
            Navigator.pop(context);
          },
          child: Text(
            "Login",
            style: TextStyle(color: Colors.red, fontSize: 16),
          ),
        ),
      ],
    );
  }
}
