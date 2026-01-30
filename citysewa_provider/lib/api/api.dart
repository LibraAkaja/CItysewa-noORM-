import "dart:convert";
import "package:http/http.dart" as http;

import "package:citysewa_provider/api/models.dart";

const baseUrl = "https://citysewa2.onrender.com/api/v1";
// const baseUrl = "http://127.0.0.1:8000/api/v1";

String parseErrorMessage(dynamic error) {
  if (error is Map) {
    for (final message in error.values) {
      if (message is List && message.isNotEmpty) {
        return message.first.toString();
      } else if (message is String) {
        return message;
      }
    }
  }
  if (error is String) {
    return error;
  }
  return "Something went wrong. Please try again.";
}

class AuthService {
  final modUrl = "accounts/provider";

  // login
  Future<LoginResponse> login(String email, String password) async {
    final body = {"email": email, "password": password};
    final url = Uri.parse("$baseUrl/$modUrl/login");
    try {
      final response = await http.post(url, body: body);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return LoginResponse(
          success: true,
          message: "Login Successful",
          user: User(
            id: data["id"],
            firstName: data["first_name"],
            lastName: data["last_name"],
            gender: data["gender"],
            verified: data["verified"],
            token: data["token"],
          ),
        );
      } else {
        final data = jsonDecode(response.body);
        final r = LoginResponse(
          success: false,
          message: parseErrorMessage(data),
        );
        return r;
      }
    } catch (e) {
      print(e);
      return LoginResponse(
        success: false,
        message: "Something went wrong. Please try again.",
      );
    }
  }

  //Register
  Future<RegisterResponse> register(
    String firstName,
    String lastName,
    String email,
    String password,
  ) async {
    final body = {
      "first_name": firstName,
      "last_name": lastName,
      "email": email,
      "password": password,
      "gender": "Male",
    };
    final url = Uri.parse("$baseUrl/$modUrl/register");
    try {
      final response = await http.post(url, body: body);

      if (response.statusCode == 200) {
        // final data = jsonDecode(response.body);
        return RegisterResponse(
          success: true,
          message: "Registration successful",
        );
      } else {
        final data = jsonDecode(response.body);
        return RegisterResponse(
          success: false,
          message: parseErrorMessage(data),
        );
      }
    } catch (e) {
      return RegisterResponse(
        success: false,
        message: "Something went wrong. Please try again.",
      );
    }
  }

  //Verify provider
  Future<VerificationResponse> verifyProvider(
    int id,
    String phoneNumber,
    String docNumber,
    String docType,
    String photoPath,
    String docPath,
  ) async {
    final url = Uri.parse("$baseUrl/$modUrl/verify");
    try {
      var request = http.MultipartRequest('POST', url);
      request.fields['id'] = id.toString();
      request.fields['phone_number'] = phoneNumber;
      request.fields['document_number'] = docNumber;
      request.fields['document_type'] = docType;

      print("photo:$photoPath");
      request.files.add(await http.MultipartFile.fromPath('photo', photoPath));
      request.files.add(await http.MultipartFile.fromPath('document', docPath));

      final responseStream = await request.send();
      final response = await http.Response.fromStream(responseStream);
      print("API11111111111111111111111111111111111111");
      if (response.statusCode == 200) {
        // final data = jsonDecode(response.body);
        print("API2222222222222222222222222222222");
        return VerificationResponse(
          success: true,
          message: "Verification successful",
        );
      } else {
        print(response.statusCode);
        print("API33333333333333333333333333333");
        print(response.body);
        print("API444444444444444444444444444444");
        final data = jsonDecode(response.body);
        return VerificationResponse(
          success: false,
          message: parseErrorMessage(data),
        );
      }
    } catch (e) {
      print("Error: $e");
      return VerificationResponse(
        success: false,
        message: "Something went wrong. Please try again.",
      );
    }
  }
}
