import telebot
import requests
import time
from keep_alive import keep_alive
keep_alive()

# Initialize your Telegram bot with the token you obtained from BotFather
bot = telebot.TeleBot("6891639487:AAHXiGM2tumJSwuYe0ydtSYQkypPE4ZnEeY")
running = True
def make_call(phone_number,message):
    url = "https://sms-call.vercel.app/api/call"
    payload = {
        "phone": phone_number
    }
    try:
        response = requests.post(url, json=payload)
        if response.json()['message'] == 'Sent':
            print(f"Call made to {phone_number} successfully!")
            bot.send_message(-1002041695132, f"Calls sent successfully to {phone_number}")
        else:
            print(f"Failed to make call to {phone_number}. Status code: {response.status_code}")
            bot.send_message(-1002041695132, f"Failed to make call to {phone_number}. error is: {response.json()['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making call to {phone_number}: {e}")
        bot.send_message(-1002041695132, f"Error occurred while making call to {phone_number}: {e}")

def make_calls(phone_numbers,message):
    global running
    for number in phone_numbers:
        if not running:
            break  
        make_call(number,message)
        

# Handle "/send" command from Telegram
@bot.message_handler(commands=['send'])
def send_messages(message):

    # Example list of phone numbers
    bot.reply_to(message, "Sending......")
    global running
    running = True
    phone_numbers = ['01101322529', '01159015092', '01141904182', '01153418345', '01207896463', '01001627450', '01067827807', '01029218735', '01024512684', '01157249594', '01024776395', '01226905327', '01063075495', '01212484146', '01063818927', '01067357476', '01140995605', '01221671561', '01023429003', '01156954028', '01128909460', '01205632766', '01287013409', '01050542336', '01062619745', '01063761346', '01227356065', '01113195508', '01154669520', '01015914094', '01210204326', '01146026712', '01113185395', '01032117812', '01288579696', '01014490590', '01015103916', '01027546387', '01143484067', '01064524404', '01098787039', '01029178704', '01063279527', '01287600577', '01156501103', '01110552110', '01015306494', '01004016751', '01121374722', '01153104619', '01123034659', '01150048739', '01064422819', '01206137526', '01014714736', '01270411954', '01120158954', '01060371169', '01223399381', '01141656497', '01066482832', '01005582641', '01006697911', '01276988118', '01098211641', '01148839093', '01141676814', '01070899021', '01271508964', '01144525014', '01050970515', '01099427585', '01112587640', '01010416325', '01018130244', '01272554934', '01095426435', '01289788437', '01113794910', '01115525850', '01204872674', '01064308389', '01063486216', '01104169818', '01158405478', '01026880548', '01147519789', '01024704709', '01021409574', '01210404152', '01124901447', '01554555715', '01212988133', '01016932469', '01021263812', '01066248974', '01025640389', '01270378002', '01050883534', '01016775389', '01274593178', '01067727606', '01095916689', '01026619459', '01558577189', '01228567642', '01150836760', '01093521377', '01144050282', '01021215983', '01552072879', '01150186400', '01003406308', '01001383082', '01062498491', '01276088469', '01227017314', '01092132596', '01019279897', '01282789951', '01126335297', '01023201714', '01271381964', '01100615989', '01015008653', '01282001839', '01007606086', '01029791277', '01154293996', '01280549289', '01011254689', '01090728558', '01276219901', '01099655149', '01550209168', '01211636065', '01155607992', '01123634649', '01067902433', '01024671837', '01012065449', '01212235136', '01097334640', '01015687104', '01015123852', '01005258300', '01287531973', '01121669778', '01068707902', '01226804672', '01006198389', '01064127274', '01223862809', '01212624552', '01278534177', '01064443853', '01019764821', '01067571932', '01557561237', '01123452948', '01273815733', '01114723681', '01028394347', '01013218769', '01212344248', '01025027297', '01006635914', '01102243283', '01003770742', '01102215579', '01284838734', '01501438155', '01212394583', '01110761267', '01157738666', '01147055221', '01022748917', '01203029615', '01093620786', '01128407895', '01210890201', '01095761662', '01212237039', '01017158823', '01203194466', '01145175159', '01221307332', '01026968092', '01022705972', '01114672418', '01229498863', '01507508773', '01228080761', '01030740787', '01096877384', '01204274208', '01200757524', '01205173903', '01008491635', '01205412889', '01093504160', '01201675858', '01026065721', '01019839144', '01145331060', '01033492947', '01147299585', '01064460839', '01279184803', '01121168603', '01220306625', '01008818620', '01272183002', '01121016609', '01142036603', '01063058953', '01208392029', '01206382003', '01015786602', '01225833594', '01097163475', '01013852000', '01113991726', '01121873756', '01101391715', '01158176446', '01112804130', '01278860814', '01157342747', '01552747497', '01206336059', '01550761456', '01100393373', '01552721004', '01001181596', '01150600875', '01064596559', '01028500798', '01065411384', '01066428478', '01067669860', '01119682554', '01201175296', '01013306748', '01095882672', '01119751360', '01203972188', '01206683408', '01027383097', '01032636533', '01212807349', '01016104535', '01278320956', '01287332955', '01147239364', '01025125326', '01551105694', '01147377808', '01278113117', '01275128183', '01286828959', '01027592030', '01150705410', '01001168618', '01002601469', '01003153496', '01003258587', '01003774092', '01003971295', '01005571121', '01006710431', '01006818808', '01008382765', '01008921102', '01009384972', '01009867351', '01010227456', '01010275023', '01012559560', '01012600814', '01012649185', '01012665040', '01013144252', '01013455908', '01013867267', '01014130690', '01014841979', '01015460168', '01016347020', '01016793588', '01016838873', '01017012033', '01020213718', '01020337858', '01020789334', '01021357924', '01021926997', '01022380252', '01022630595', '01023114793', '01024055659', '01024138495', '01024658394', '01024690960', '01025142387', '01025282518', '01026452169', '01026791956', '01028616389', '01029169863', '01029294604', '01029929583', '01030397158', '01030665989', '01030717473', '01030771813', '01030848136', '01030965338', '01032153540', '01032535014', '01033446143', '01033777197', '01050439220', '01050666121', '01061326649', '01061641043', '01061693231', '01061821314', '01062010760', '01062831310', '01063202488', '01063980172', '01064972658', '01066382496', '01066394986', '01066715042', '01066867709', '01067673682', '01067957966', '01068036202', '01068592102', '01070463657', '01080716127', '01090785501', '01090976894', '01091198567', '01091956366', '01092429973', '01093586107', '01093835376', '01093848838', '01094628241', '01094861307', '01095350890', '01095885138', '01096620368', '01096841430', '01097011113', '01097057354', '01097261935', '01099120381', '01110294614', '01110411559', '01113474423', '01114566381', '01116785756', '01117814527', '01119785690', '01120993719', '01122054931', '01124807818', '01125132864', '01125203553', '01125835950', '01126183142', '01126431078', '01126724218', '01127138473', '01127650274', '01128261658', '01129188146', '01129688705', '01129781129', '01142452803', '01142571156', '01143510655', '01144083159', '01144452480', '01145203286', '01146018054', '01146791239', '01149426857', '01150405527', '01150836738', '01154287326', '01156123646', '01156186032', '01156299948', '01156471419', '01157588486', '01158396459', '01158958429', '01200767860', '01200805134', '01201069745', '01201196462', '01201724235', '01204847221', '01205275199', '01205365797', '01206168482', '01206778257', '01207538309', '01207712087', '01207987024', '01208229387', '01208831059', '01208868495', '01211219154', '01211290147', '01211956570', '01220032297', '01220796396', '01221412306', '01221630421', '01223163499', '01224515249', '01225974549', '01225985802', '01226207536', '01226236996', '01226245093', '01226251568', '01226477461', '01226868275', '01227227464', '01227598157', '01229711243', '01229729545', '01270471133', '01271253571', '01271640637', '01272300913', '01272876968', '01272943987', '01273519150', '01273631750', '01274109838', '01274736273', '01275264242', '01276442038', '01278138175', '01278552296', '01278561026', '01279368533', '01280183185', '01280373847', '01280758217', '01281468592', '01281516399', '01282559066', '01284733284', '01286410690', '01287545494', '01289475644', '01551510330', '01552121992', '01552179699', '01552498861', '01553484914', '01554027004', '01555791224']
    make_calls(phone_numbers,message)
    bot.reply_to(message, "Done sent calls successfully!")
@bot.message_handler(commands=['start'])
def send_messages(message):

    bot.send_message(-1002041695132, "/send دوس هنا عشان تبعت المكالمات ")

@bot.message_handler(commands=['stop'])
def stop_messages(message):
    global running
    running = False
    bot.reply_to(message, "Send Call stopped!")

# Start the bot
bot.polling()


