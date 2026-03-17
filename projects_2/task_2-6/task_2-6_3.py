def blood_group():
    sovmest = {
        "0": "0, A, B, AB",
        "A": "A, AB",
        "B": "B, AB",
        "AB": "AB"
    }
    
    donor = input("Группа донора (0, A, B, AB): ").upper()
    patient = input("Группа пациента (0, A, B, AB): ").upper()
    
    if patient in compatible[donor]:
        print("Совместимы")
    else:
        print("Несовместимы")
        print(f"Для пациента {patient} подходят доноры: {sovmest[patient]}")

blood_group()
