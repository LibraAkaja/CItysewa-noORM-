import "package:flutter/material.dart";
// import "package:shared_preferences/shared_preferences.dart"
//     show SharedPreferences;

import 'package:citysewa_provider/screens/profile_screen.dart'
    show ProfileScreen;

class HomeScreen extends StatefulWidget {
  HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          toolbarHeight: 48,
          leading: ProfileIcon(),
          titleSpacing: 0,
          titleTextStyle: Theme.of(context).textTheme.titleMedium,
          title: Text(
            "Ravi Kumar",
            style: TextStyle(fontSize: 15),
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
          centerTitle: false,
          actions: [
            IconButton(
              onPressed: () {},
              icon: Icon(Icons.notifications, color: Colors.black, size: 32),
            ),
          ],
        ),
        body: Padding(
          padding: EdgeInsets.all(10),
          child: ListView(children: [BookingSection()]),
        ),
        bottomNavigationBar: BottomNavigationBar(
          items: [
            BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
            BottomNavigationBarItem(icon: Icon(Icons.book), label: "Bookings"),
            BottomNavigationBarItem(
              icon: Icon(Icons.miscellaneous_services_rounded),
              label: "Services",
            ),
            BottomNavigationBarItem(icon: Icon(Icons.person), label: "Profile"),
          ],
        ),
      ),
    );
  }
}

class ProfileIcon extends StatelessWidget {
  ProfileIcon({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(8),
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => ProfileScreen()),
          );
        },
        child: CircleAvatar(
          radius: 16,
          backgroundColor: Colors.white,
          backgroundImage: AssetImage('assets/images/test.png'),
        ),
      ),
    );
  }
}

class BookingSection extends StatefulWidget {
  BookingSection({super.key});

  @override
  State<BookingSection> createState() => _BookingSectionState();
}

class _BookingSectionState extends State<BookingSection> {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color.fromARGB(255, 212, 234, 249),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(30),
            blurRadius: 14,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Bookings",
            style: Theme.of(
              context,
            ).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 12),
          Row(
            spacing: 10,
            children: const [
              Expanded(
                child: BookingCard(
                  title: "Completed",
                  value: 3,
                  titleIcon: Icons.check_circle_outline,
                ),
              ),

              Expanded(
                child: BookingCard(
                  title: "Pending",
                  value: 5,
                  titleIcon: Icons.pending_actions_rounded,
                ),
              ),

              Expanded(
                child: BookingCard(
                  title: "Active",
                  value: 0,
                  titleIcon: Icons.auto_mode_outlined,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class BookingCard extends StatelessWidget {
  final String title;
  final int value;
  final IconData titleIcon;
  const BookingCard({
    super.key,
    required this.title,
    required this.value,
    required this.titleIcon,
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {},
      child: Container(
        padding: EdgeInsets.all(5),
        height: 100,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(10),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withAlpha(50),
              blurRadius: 10,
              offset: Offset(0, 6),
            ),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              spacing: 5,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  title,
                  style: TextStyle(
                    color: Colors.grey,
                    fontSize: 14,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                Icon(titleIcon, size: 16, color: Colors.grey),
              ],
            ),
            Text(
              "$value",
              style: TextStyle(
                color: Colors.deepOrange,
                fontSize: 32,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
