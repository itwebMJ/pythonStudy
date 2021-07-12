import businfo.BusService as b_info

def printVo(vo):
    if vo == None:
        print('검색안됨')
    else:
        print(vo)

def printList(vo_list):
    if vo_list == None:
        print('검색안됨')
    else:
        for v in vo_list:
            print(v)

def main():
    b_service = b_info.BusService()
    #vo = b_service.getRouteInfoItem('100100124')
    #vo_list = b_service.getRoutePathList('100100124')
    #vo_list = b_service.getBusRouteList('0017')

    vo_list = b_service.getStaionsByRouteList('100100124')

    #printVo(vo)
    printList(vo_list)

main()
