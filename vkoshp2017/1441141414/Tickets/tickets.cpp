#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Tickets
{
	int seconds;
	int type;
	Tickets(int ticket_seconds, int ticket_type) : seconds(ticket_seconds), type(ticket_type) {}
	Tickets() : seconds(0), type(0) {}
	bool operator <(const Tickets &ticket) const {
		return (seconds < ticket.seconds) || ((seconds == ticket.seconds) && (type < ticket.type));
	}

};


const int MAXSEC = 86400;
vector<Tickets> tickets;

int main() {
	int n;
	int n_around_the_clock = 0;
	int first, first_hours, first_min, first_sec;
	int second, second_hours, second_min, second_sec;

	cin >> n;


	for (int i = 0; i < n; ++i) {
		cin >> first_hours >> first_min >> first_sec;
		cin >> second_hours >> second_min >> second_sec;                //tak vvod ponyatnee prosto
		
		first = ((first_hours * 60) + first_min) * 60 + first_sec;
		second = ((second_hours * 60) + second_min) * 60 + second_sec;
		
		if (second < first) {
			tickets.emplace_back(first, -1);
			tickets.emplace_back(MAXSEC, 1);
			
			tickets.emplace_back(0, -1);
			tickets.emplace_back(second, 1);
		}
		else if (second == first) {
			n_around_the_clock++;
		}
		else {

			tickets.emplace_back(first, -1);
			tickets.emplace_back(second, 1);
		}
	}
	stable_sort(tickets.begin(), tickets.end());
	
	int ans = 0;
	int res = 0;
	int cnt = 0;
	bool is_started = false;
	if (n_around_the_clock != n) {
		for (int i = 0; i < (int)tickets.size(); ++i) {
			cnt += tickets[i].type;
			if (cnt == (n_around_the_clock - n) && !is_started) {
				res = i;
				is_started = true;
			}
			if (cnt != (n_around_the_clock - n) && is_started) {
				ans += tickets[i].seconds - tickets[res].seconds;
				is_started = false;
			}
		}
	}
	else {
		ans = MAXSEC;
	}
	cout << ans;
	return 0;
}