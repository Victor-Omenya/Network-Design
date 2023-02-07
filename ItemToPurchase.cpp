#include <iostream>
#include "ItemToPurchase.h"
using namespace std;

ItemToPurchase::ItemToPurchase() : itemName("none"), itemPrice(0), itemQuantity(0), itemDescription("none") {}

void ItemToPurchase::SetName(string userName) {
	itemName = userName;
}

string ItemToPurchase::GetName() {
	return itemName;
}

void ItemToPurchase::SetPrice(int userPrice) {
	itemPrice = userPrice;
}

int ItemToPurchase::GetPrice() {
	return itemPrice;
}

void ItemToPurchase::SetQuantity(int userQuantity) {
	itemQuantity = userQuantity;
}

int ItemToPurchase::GetQuantity() {
	return itemQuantity;
}

void ItemToPurchase::SetDescription(string userDescription) {
	itemDescription = userDescription;
}

string ItemToPurchase::GetDescription() {
	return itemDescription;
}

void ItemToPurchase::PrintItemCost() {
	cout << itemName << " " << itemQuantity << " @ $" << itemPrice << " = $" << itemQuantity * itemPrice << endl;
}

void ItemToPurchase::PrintItemDescription() {
	cout << itemName << ": " << itemDescription << "." << endl;
}
