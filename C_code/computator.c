#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


#define DEGREE_TO_RADIAN(degrees) ((degrees) * M_PI / 180.0)

// axis stands for 'x' or 'y', determining the needed equation
// (initial_coordinate_axis and initial_velocity_axis) correspond to (x and Vx) or (y and Vy)
// returns m, x or y coordinate
double analytical_equations(char axis, double initial_coordinate_axis, double initial_velocity_axis, double time, double g) {
	if (axis == 'x') {
		double Vi_x = initial_velocity_axis;
		double x_i = initial_coordinate_axis;
		return (x_i + Vi_x * time);
	}
	else if (axis == 'y') {
		double Vi_y = initial_velocity_axis;
		double y_i = initial_coordinate_axis;
		return (y_i + Vi_y * time - 1.0 / 2.0 * g * time * time);
	}
}

// axis stands for 'x' or 'y', determining the needed equation
// returns m/s^2, acceleration
double differential_equations(char axis, double beta, double vx, double vy, double g) {
	if (axis == 'x') {
		double root = sqrt(vx * vx + vy * vy);
		return (-beta * vx * root);
	}
	else if (axis == 'y') {
		double root = sqrt(vx * vx + vy * vy);
		return (-g - beta * vy * root);
	}
}


int main() {
	// initialization, then values are taken from input.txt
	// comments explanation: unit ; letter
	double mass = 0; // kg ; m
	double head_surface = 0; // m^2 ; A
	double air_resistance_coefficient = 0; // . ; Cd
	double delta_air_time = 0; // s ; dt
	double initial_velocity = 0; // m/s ; Vi
	double cannon_angle = 0; // degrees ; alpha
	char analytical_solution_needed = 0;

	// inputted by user
	FILE* input_file = fopen("../computational_files_io/input.txt", "r");
	if (input_file == NULL) {
		return -1;
	}

	char line[256];
	int valueCount = 0;

	while (fgets(line, sizeof(line), input_file) != NULL && valueCount < 8) {
		// skip lines starting with '#'
		if (line[0] == '#') {
			continue;
		}

		if (valueCount == 0) {
			mass = strtod(line, NULL);
		}
		else if (valueCount == 1) {
			head_surface = strtod(line, NULL);
		}
		else if (valueCount == 2) {
			air_resistance_coefficient = strtod(line, NULL);
		}
		else if (valueCount == 3) {
			initial_velocity = strtod(line, NULL);
		}
		else if (valueCount == 4) {
			cannon_angle = strtod(line, NULL);
		}
		else if (valueCount == 5) {
			delta_air_time = strtod(line, NULL);
		}
		else if (valueCount == 6) {
			if (strcmp(line, "YES\n") != 0) {
				// don't account for air drag in numerical solution
				mass = 0;
				air_resistance_coefficient = 0;
				head_surface = 0;
			}
		}
		else if (valueCount == 7) {
			if (strcmp(line, "YES\n") == 0) {
				analytical_solution_needed = 1;
			}
			else {
				analytical_solution_needed = 0;
			}
		}
		valueCount++;
	}

	fclose(input_file);

	// default
	double grav_acceleration = 9.80665; // m/s^2
	double air_density = 1.225; // kg/m^3 ; p  - atmospheric conditions

	// initial conditions & calculations
	double aerodyn_drag_coefficient;
	if (air_resistance_coefficient != 0 && mass != 0 && head_surface != 0) {
		aerodyn_drag_coefficient = (air_density * air_resistance_coefficient * head_surface) / (2 * mass);
	}
	else {
		aerodyn_drag_coefficient = 0;
	}

	double initial_x_coord = 0.0, initial_y_coord = 0.0; // m
	double x_coord = initial_x_coord, y_coord = initial_y_coord; // m
	double analytical_x_coord = initial_x_coord, analytical_y_coord = initial_y_coord; // m

	double initial_velocity_x = initial_velocity * cos(DEGREE_TO_RADIAN(cannon_angle)); // m/s ; Vix
	double initial_velocity_y = initial_velocity * sin(DEGREE_TO_RADIAN(cannon_angle)); // m/s ; Viy
	double velocity_x = initial_velocity_x; // m/s ; Vx
	double velocity_y = initial_velocity_y; // m/s ; Vy

	double air_time = 0.0; // s ; t

	// txt output
	FILE* output_file = fopen("../computational_files_io/output.txt", "w");
	if (output_file == NULL) {
		return -1;
	}

	// different print to output.txt depending on if analytical solution is needed
	if (analytical_solution_needed) {
		fprintf(output_file, "x\ty\t|\tx_an\ty_an\n");
		fprintf(output_file, "%lf\t%lf\t|\t%lf\t%lf\n", x_coord, y_coord, analytical_x_coord, analytical_y_coord);
	}
	else {
		fprintf(output_file, "x\ty\n");
		fprintf(output_file, "%lf\t%lf\n", x_coord, y_coord);
	}

	do {
		// Runge-Kutta-4th method
		if (y_coord >= 0) {
			// dvx, dvy - stands for delta velocity_x and delta velocity_y
			double k1_dvx = delta_air_time * differential_equations('x', aerodyn_drag_coefficient, velocity_x, velocity_y, grav_acceleration);
			double k1_dvy = delta_air_time * differential_equations('y', aerodyn_drag_coefficient, velocity_x, velocity_y, grav_acceleration);

			double k2_dvx = delta_air_time * differential_equations('x', aerodyn_drag_coefficient, velocity_x + 0.5 * k1_dvx, velocity_y + 0.5 * k1_dvy, grav_acceleration);
			double k2_dvy = delta_air_time * differential_equations('y', aerodyn_drag_coefficient, velocity_x + 0.5 * k1_dvx, velocity_y + 0.5 * k1_dvy, grav_acceleration);

			double k3_dvx = delta_air_time * differential_equations('x', aerodyn_drag_coefficient, velocity_x + 0.5 * k2_dvx, velocity_y + 0.5 * k2_dvy, grav_acceleration);
			double k3_dvy = delta_air_time * differential_equations('y', aerodyn_drag_coefficient, velocity_x + 0.5 * k2_dvx, velocity_y + 0.5 * k2_dvy, grav_acceleration);

			double k4_dvx = delta_air_time * differential_equations('x', aerodyn_drag_coefficient, velocity_x + k3_dvx, velocity_y + k3_dvy, grav_acceleration);
			double k4_dvy = delta_air_time * differential_equations('y', aerodyn_drag_coefficient, velocity_x + k3_dvx, velocity_y + k3_dvy, grav_acceleration);

			velocity_x += (k1_dvx + 2.0 * k2_dvx + 2.0 * k3_dvx + k4_dvx) / 6.0;
			velocity_y += (k1_dvy + 2.0 * k2_dvy + 2.0 * k3_dvy + k4_dvy) / 6.0;

			x_coord += velocity_x * delta_air_time;
			y_coord += velocity_y * delta_air_time;
		}

		air_time += delta_air_time;

		// different print to output.txt depending on if analytical solution is needed
		if (analytical_solution_needed) {
			analytical_x_coord = analytical_equations('x', initial_x_coord, initial_velocity_x, air_time, grav_acceleration);
			analytical_y_coord = analytical_equations('y', initial_y_coord, initial_velocity_y, air_time, grav_acceleration);

			fprintf(output_file, "%lf\t%lf\t|\t%lf\t%lf\n", x_coord, y_coord, analytical_x_coord, analytical_y_coord);
		}
		else {
			fprintf(output_file, "%lf\t%lf\n", x_coord, y_coord);
		}

	} while (y_coord > 0 || (analytical_y_coord > 0 && analytical_solution_needed));

	fclose(output_file);

	return 0;
}