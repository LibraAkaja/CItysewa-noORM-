class LoginResponse {
  bool success = false;
  String message;
  User? user;

  LoginResponse({required this.success, required this.message, this.user});
}

class RegisterResponse {
  bool success = false;
  String message;

  RegisterResponse({required this.success, required this.message});
}

class VerificationResponse {
  bool success = false;
  String message;

  VerificationResponse({required this.success, required this.message});
}

class User {
  final int id;
  final String firstName;
  final String lastName;
  final String gender;
  bool verified;
  String token;

  User({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.gender,
    required this.verified,
    required this.token,
  });
}

final loginRes = {
  "id": 4,
  "created_at": "2026-01-28T11:16:07.787042Z",
  "updated_at": "2026-01-28T11:16:07.787042Z",
  "user_id": 22,
  "first_name": "Ravi",
  "last_name": "Kumar",
  "gender": "Male",
  "verified": false,
  "token": "e3f6bfe94404761d35e31415bcc8101c6f0794da",
};
