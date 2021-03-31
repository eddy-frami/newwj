import unittest
import requests
import json
from globle import globle1
g2 = globle1()
class addact01(unittest.TestCase):
	addurl = "http://0.0.0.0:16200/sdb/openApi/hmf/v1/merchAdd/addAccount"
	addata = {
		"header": {
			"version": "1.0",
			"platform": "hm",
			"method": "sdb/openApi/hmf/v1/merchAdd/addAccount",
			"contentType": "text/plain;charset=UTF-8",
			"sign": "",
			"signMethod": "",
			"sequenceId": "12345678965412",
			"reqTime": "20190513112830",
			"reserve": ""
		},
		"body": {
			"orderCode": "19012309000200000003",
			"channelId": "0001",
			"shopLinkmanAreaCode": "0375",
			"shopLinkmanTel": "99999990",
			"shopLinkmanMail": "fref0@163.com",
			"serviceTel": "18522223330",
			"reserved": "123450",
			"inAccountAttr": "0",
			"inAccountNo": "123456780",
			"inAccountName": "110",
			"merchInfo": {
				"shopNo": "",
				"legalPhone": "17721310417",
				"shopRegName": "商户注册名称河马付第40",
				"shopNickName": "商户简称河马付2502",
				"shopOperateAddr": "经营地址河马付2402",
				"businessScope": "4900",
				"businessDepict": "主营业务场景描述河马付2402",
				"shopType": "1",
				"registCost": "10000",
				"registDate": "2019-01-01",
				"shopRegPost": "888999",
				"icpNo": "1111112222220",
				"holdPeople": "实际控股人0",
				"shopCorp": "法法人姓名0",
				"userSex": "2",
				"userNationalityFlg": "2",
				"corpCretType": "1",
				"corpCretNo": "410423199104151545",
				"corpValidityType": "2",
				"corpStartDate": "20190101",
				"corpExpiryDate": "20290101",
				"bmBusinessLicense": {
					"businessLicense": "110108001446041001",
					"businessLicenseType": "4",
					"licenseValidityType": "2",
					"licenseStartDate": "2019-01-01",
					"licenseExpiryDate": "2098-01-01",
				},
				"merch_image": [{
					"imgSysNo": "6785709",
				}, {
					"imgSysNo": "6785710",

				}, {
					"imgSysNo": "6785711",
				}, {
					"imgSysNo": "6785712",
				}, {
					"imgSysNo": "6785713",
				}],

			},
			"hmfShopNo": "S8991640",
			"source": "0002",
			"shopOperateName": "商户经营名称02",
			"signFrom": "1",
			"subComp": "1",
			"signUser": "1",
			"agentSignSysNo": "1",
			"td0CreditMonery": "100000",
			"signRemark": "qianyue签约beizhu签约备注02",
			"keyRecInfo": {
				"keyRecipients": "联系02",
				"keyRecAddress": "联系人地址02",
				"keyRecPhone": "17700000002",
				"keyRecPostcode": "123450",
				"keyRecCardNo": "410423199104161618",
			},
			"tradeType": "2",
			"payAccountInfos": [{
				"accountName": "结算账号02",
				"accountBank": "1 ",
				"accountBankCode": "103290036068",
				"account": "6228480038048409875",
				"account_image": [{"a": "1"}]
			}],
			"scrInfos": {
				"idNo": "301819458",
				"regStrentDoor": "公司注册地址街道地址02",
				"regDist": "330102000000",
				"taxRegNo": "12510000450717578Y"

			}
		}
	}

	def addac0101(self):
		self.addata['body']['orderCode'] = g2.get_value('orderCode')
		self.addata['body']['merchInfo']['shopRegName'] = g2.get_value('shopRegName')
		self.addata['body']['merchInfo']['bmBusinessLicense']['businessLicense'] = g2.get_value('businessLicense')
		# self.addata['body']['payAccountInfos']['account'] = g2.get_value('account1')
		self.addata['body']['hmfShopNo'] = g2.get_value('hmfShopNo')
		self.addata['body']['scrInfos']['idNo'] = g2.get_value('idNo')
		# self.addata['shopRegName'] = globals().get('shopRegName') or self.addata['shopRegName']
		# self.addata['orderCode'] = globals().get('orderCode') or self.addata['orderCode']
		# self.addata['businessLicense'] = globals().get('businessLicense') or self.addata['businessLicense']
		# self.addata['hmfShopNo'] = globals().get('hmfShopNo') or self.addata['hmfShopNo']
		# self.addata['idNo'] = globals().get('idNo') or self.addata['idNo']
		response = requests.post(url=self.addurl, data=json.dumps(self.addata),
								 headers={'Content-Type': 'application/json'})
		print(response.text)














