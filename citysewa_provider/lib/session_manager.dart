import "package:shared_preferences/shared_preferences.dart";

import "package:citysewa_provider/api/models.dart" show User;

class SessionManager {
  static Future saveUser(User user) async {
    final prefs = await SharedPreferences.getInstance();

    prefs.setInt("id", user.id);
    prefs.setString("firstName", user.firstName);
    prefs.setString("lastName", user.lastName);
    prefs.setString("gender", user.gender);
    prefs.setBool("verified", user.verified);
    prefs.setString("token", user.token);
  }

  static Future<User?> getUser() async {
    final prefs = await SharedPreferences.getInstance();

    final id = prefs.getInt("id");
    if (id == null) return null;
    final firstName = prefs.getString("firstName");
    final lastName = prefs.getString("lastName");
    final gender = prefs.getString("gender");
    final verified = prefs.getBool("verified");
    final token = prefs.getString("token");

    return User(
      id: id,
      firstName: firstName!,
      lastName: lastName!,
      gender: gender!,
      verified: verified!,
      token: token!,
    );
  }

  static Future logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.clear();
  }
}
