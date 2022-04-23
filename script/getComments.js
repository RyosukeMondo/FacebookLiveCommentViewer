var classCommId = "tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41";
var classCommText = "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql";
var classReadMore = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p";
var texts = [];
var as = document.getElementsByTagName("a");
for(var idx = 0; idx < as.length; idx++){
    var links = as[idx].getElementsByClassName(classCommId);
    if( links.length > 0 ) {
        var commId = as[idx].href;
        var commElem = as[idx]
            .parentElement.parentElement.parentElement
            .getElementsByClassName(classCommText)[0];
        var mores = commElem.getElementsByClassName(classReadMore);
        if( mores.length > 0){ 
            if(mores[0].innerText?.match(/もっと見る/)){
                mores[0].click();
            }
        }
        var comm = commElem.innerText
            .replaceAll("\r\n","")
            .replaceAll("\n","")
            .replaceAll("\r","")
            .replaceAll("<","")
            .replaceAll(">","")
            .replaceAll("&","")
            .replaceAll("\"","")
            .replaceAll("'","")
            ;
        //console.log(commElem.innerText);
        texts.push(commId + "," + comm);
        //console.log(texts.length);
    }
}
return texts.join("\n");