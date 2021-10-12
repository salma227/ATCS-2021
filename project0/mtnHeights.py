mtnHeights = {'K2': '28,251',
              'Makalu': '27,838',
              'Broad Peak': '26,414',
              'Kamet': '25,446',
              'The Crown': '23,934'}
for mtn in mtnHeights.keys():
    print(mtn)
for mt in mtnHeights.values():
    print(mt)
for mtn, h in mtnHeights.items():
    print(mtn+" is "+h+" ft tall.")
