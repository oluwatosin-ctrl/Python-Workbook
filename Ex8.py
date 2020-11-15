WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

NO_GIZMO = int(input("Enter no of gizmo"))
NO_WIDGET = int(input("Enter no of widgets"))

TOTAL_COST = int((WIDGET_WEIGHT*NO_WIDGET)+(GIZMO_WEIGHT*NO_GIZMO))

print("The total weight of the order is",TOTAL_COST)