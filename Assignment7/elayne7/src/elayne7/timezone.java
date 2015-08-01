package elayne7;

import javax.swing.JOptionPane;
import org.geonames.WebService;
import org.geonames.Timezone;

public class timezone {
	public static void main(String[] args) {
		// Welcome message
		System.out.println("Elayne Delgado - Assignment 7 - Timezone");

		// Grab user information
		double latitude = Double.parseDouble(JOptionPane
				.showInputDialog("Enter latitude:"));
		double longitude = Double.parseDouble(JOptionPane
				.showInputDialog("Enter longitude:"));

		// Set webservice username
		WebService.setUserName("demo");

		try {
			// Pull information
			Timezone t = WebService.timezone(latitude, longitude);

			// Print out information
			System.out.println("Timezone ID: " + t.getTimezoneId());
			System.out.println("Country Code: " + t.getCountryCode());
			System.out.println("Time: " + t.getTime());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
