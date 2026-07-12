def presenteer(mijn_dict, totaal):
    for key, value in mijn_dict.items():
        print(f"{key}: {value}")
    print("="*25)
    print(f"Totaal: {totaal}")

mijn_dict = {"vis": 10, "vlees": 25, "overig": 15}
totaal = 50

presenteer(mijn_dict, totaal)

