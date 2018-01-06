#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlwt


if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('doubantop250', cell_overwrite_ok=False)
    worksheet.write(1, 5, 'gg')
    worksheet.write(1, 6, 'hhh')
    workbook.save('test.xls')