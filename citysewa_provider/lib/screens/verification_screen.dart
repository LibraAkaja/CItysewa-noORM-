import "package:flutter/material.dart";
import "package:image_picker/image_picker.dart";

import 'package:citysewa_provider/api/api.dart' show AuthService;
import 'package:citysewa_provider/api/models.dart' show User;
import 'package:citysewa_provider/session_manager.dart' show SessionManager;

final auth = AuthService();

class VerificationScreen extends StatefulWidget {
  const VerificationScreen({super.key});

  @override
  State<VerificationScreen> createState() => _VerificationScreenState();
}

class _VerificationScreenState extends State<VerificationScreen> {
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
      appBar: AppBar(),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          children: [
            Text("Fill out this verification form."),
            SizedBox(height: 5),
            VerificationForm(user),
          ],
        ),
      ),
    );
  }
}

class VerificationForm extends StatefulWidget {
  final User? user;
  const VerificationForm(this.user, {super.key});

  @override
  State<VerificationForm> createState() => _VerificationFormState();
}

class _VerificationFormState extends State<VerificationForm> {
  bool isLoading = false;
  String? photoPath;
  String? docPath;
  String photoLabel = "Upload your photo";
  String docLabel = "Upload document";
  List<String> documentType = [
    'Citizenship',
    'Driving Liscense',
    'Voter ID',
    'National ID',
  ];
  String? selectedDocumentType;
  TextEditingController phoneController = TextEditingController();
  TextEditingController docNoController = TextEditingController();

  @override
  void dispose() {
    phoneController.dispose();
    docNoController.dispose();
    super.dispose();
  }

  Future<XFile?> getImage() async {
    final ImagePicker picker = ImagePicker();
    final XFile? image = await picker.pickImage(source: ImageSource.gallery);
    return image;
  }

  Future getPhoto() async {
    final XFile? photo = await getImage();
    if (photo != null) {
      setState(() {
        photoPath = photo.path;
        photoLabel = photo.name;
      });
    }
  }

  Future getDoc() async {
    final XFile? doc = await getImage();
    if (doc != null) {
      setState(() {
        docPath = doc.path;
        docLabel = doc.name;
      });
    }
  }

  Future<void> submitForm() async {
    setState(() {
      isLoading = true;
    });
    final phoneNumber = phoneController.text.toString();
    final docNumber = docNoController.text.toString();
    final docType = selectedDocumentType;
    if (phoneNumber.isEmpty ||
        docNumber.isEmpty ||
        docType == null ||
        photoPath == null ||
        docPath == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Center(
            child: Text(
              "Please make sure all fields are filled out correctly.",
              style: TextStyle(fontSize: 16),
            ),
          ),
        ),
      );
    } else {
      final result = await auth.verifyProvider(
        widget.user!.id,
        phoneNumber,
        docNumber,
        docType,
        photoPath!,
        docPath!,
      );
      if (result.success) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            backgroundColor: Colors.green,
            content: Center(child: Text(result.message)),
          ),
        );
      } else {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(SnackBar(content: Center(child: Text(result.message))));
      }
    }

    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 15, horizontal: 10),
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(width: 1, color: Colors.grey),
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(30),
            offset: Offset(0, 6),
            blurRadius: 6,
          ),
        ],
      ),
      child: Column(
        spacing: 10,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text("Verify yourself", style: TextStyle(fontSize: 16)),
          TextField(
            controller: phoneController,
            keyboardType: TextInputType.phone,
            decoration: InputDecoration(hintText: 'Phone Number'),
          ),
          LayoutBuilder(
            builder: (context, constraints) {
              return DropdownMenuFormField<String>(
                enableSearch: false,
                hintText: 'Select a document type',
                width: double.infinity,
                menuStyle: MenuStyle(
                  minimumSize: WidgetStateProperty.all(
                    Size(constraints.maxWidth, 0),
                  ),
                  maximumSize: WidgetStateProperty.all(
                    Size(constraints.maxWidth, 400),
                  ),
                ),
                dropdownMenuEntries: documentType.map(buildMenuItem).toList(),
                onSelected: (value) {
                  setState(() => selectedDocumentType = value!);
                },
              );
            },
          ),

          TextField(
            controller: docNoController,
            decoration: InputDecoration(hintText: 'Document number'),
          ),
          Wrap(
            spacing: 10,
            runSpacing: 10,
            children: [
              OutlinedButton.icon(
                onPressed: () {
                  getPhoto();
                },
                label: Text(
                  photoLabel.length > 20
                      ? photoLabel.substring(0, 20)
                      : photoLabel,
                ),
                icon: Icon(Icons.add_a_photo_rounded),
              ),
              OutlinedButton.icon(
                onPressed: () {
                  getDoc();
                },
                label: Text(
                  docLabel.length > 20 ? docLabel.substring(0, 20) : docLabel,
                ),
                icon: Icon(Icons.document_scanner),
              ),
            ],
          ),
          TextButton(
            onPressed: () {
              submitForm();
            },
            style: ButtonStyle(
              side: WidgetStateProperty.all(
                BorderSide(width: 1, color: Colors.grey),
              ),
            ),
            child: isLoading
                ? SizedBox(
                    height: 20,
                    width: 20,
                    child: CircularProgressIndicator(strokeWidth: 3),
                  )
                : Text("Submit"),
          ),
        ],
      ),
    );
  }

  DropdownMenuEntry<String> buildMenuItem(String item) =>
      DropdownMenuEntry(value: item, label: item);
}
