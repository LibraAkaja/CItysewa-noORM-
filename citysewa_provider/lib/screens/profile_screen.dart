import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class ProfileScreen extends StatefulWidget {
  ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(10),
        child: ListView(
          children: [
            SizedBox(height: 10),
            Header(),
            SizedBox(height: 20),
            VerificationForm(),
          ],
        ),
      ),
    );
  }
}

class Header extends StatefulWidget {
  Header({super.key});

  @override
  State<Header> createState() => _HeaderState();
}

class _HeaderState extends State<Header> {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: const Color.fromARGB(255, 185, 220, 246),
        borderRadius: BorderRadius.circular(16),
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
                Text(
                  "Ravi Kumar",
                  style: TextStyle(fontSize: 16, color: Colors.black),
                ),
                Text(
                  "Carpenter",
                  style: TextStyle(fontSize: 14, color: Colors.grey),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class VerificationForm extends StatefulWidget {
  VerificationForm({super.key});

  @override
  State<VerificationForm> createState() => _VerificationFormState();
}

class _VerificationFormState extends State<VerificationForm> {
  List<String> documentType = [
    'Citizenship',
    'Driving Liscense',
    'Voter ID',
    'National ID',
  ];
  String selectedDocumentType = 'Citizenship';

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
            keyboardType: TextInputType.phone,
            decoration: InputDecoration(hintText: 'Phone Number'),
          ),
          LayoutBuilder(
            builder: (context, constraints) {
              return DropdownMenuFormField<String>(
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

          TextField(decoration: InputDecoration(hintText: 'Document number')),
          Wrap(
            spacing: 10,
            runSpacing: 10,
            children: [
              OutlinedButton.icon(
                onPressed: () {},
                label: Text("Upload your photo"),
                icon: Icon(Icons.add_a_photo_rounded),
              ),
              OutlinedButton.icon(
                onPressed: () {},
                label: Text("Upload document"),
                icon: Icon(Icons.document_scanner),
              ),
            ],
          ),
        ],
      ),
    );
  }

  DropdownMenuEntry<String> buildMenuItem(String item) =>
      DropdownMenuEntry(value: item, label: item);
}
