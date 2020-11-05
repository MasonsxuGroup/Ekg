package main;

import java.util.Iterator;

import org.apache.jena.graph.Triple;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.RDFNode;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.StmtIterator;
import org.apache.jena.reasoner.InfGraph;
import org.apache.jena.reasoner.rulesys.GenericRuleReasoner;
import org.apache.jena.reasoner.rulesys.GenericRuleReasonerFactory;
import org.apache.jena.reasoner.rulesys.Rule;
import org.apache.jena.util.PrintUtil;
import org.apache.jena.vocabulary.RDFS;

public class xgfytuili {
	public static void main (String args[]) {
		Model myMod = ModelFactory.createDefaultModel();
		String xgfy = "http://www.example.org/xgfy#";
		//设置事件类
		Resource 新冠肺炎 = myMod.createResource(xgfy + "新冠肺炎");
		Resource 疫情变化 = myMod.createResource(xgfy + "疫情变化");
		Resource 国家政策和举措 = myMod.createResource(xgfy + "国家政策和举措");
		Resource 湖北省政策和举措 = myMod.createResource(xgfy + "湖北省政策和举措");
		Resource 武汉市政策和举措 = myMod.createResource(xgfy + "武汉市政策和举措");
		Resource 其他省市政策和举措 = myMod.createResource(xgfy + "其他省市政策和举措");
		Resource 国际举措 = myMod.createResource(xgfy + "国际举措");
		Resource 社会关注问题 = myMod.createResource(xgfy + "社会关注问题");
		
		//测试推理
		Resource 黄石市政策和举措 = myMod.createResource(xgfy + "黄石市政策和举措");
		
		
		//设置关系
		Property 并列关系 = myMod.createProperty(xgfy + "并列关系");
		Property 组成关系 = myMod.createProperty(xgfy + "组成关系");
		Property 跟随关系 = myMod.createProperty(xgfy + "跟随关系");
		Property 因果关系 = myMod.createProperty(xgfy + "因果关系");
		Property 并发关系 = myMod.createProperty(xgfy + "并发关系");
		//设置事件
		Resource 国务院2020年4月4日举行全国性哀悼活动 = myMod.createResource(xgfy + "国务院2020年4月4日举行全国性哀悼活动");
		Resource 党中央成立应对疫情工作领导小组 = myMod.createResource(xgfy + "党中央成立应对疫情工作领导小组");
		Resource 湖北省启动突发公共事件一级响应 = myMod.createResource(xgfy + "湖北省启动突发公共事件一级响应");
		Resource 湖北省红十字会3名领导被问责 = myMod.createResource(xgfy + "湖北省红十字会3名领导被问责");
		Resource 在2020年湖北省两会召开 = myMod.createResource(xgfy + "在2020年湖北省两会召开");
		Resource 武汉宣布封城 = myMod.createResource(xgfy + "武汉宣布封城");
		Resource 武汉新建两所医院火神山和雷神山 = myMod.createResource(xgfy + "武汉新建两所医院火神山和雷神山");
//		Resource 武汉解封 = myMod.createResource(xgfy + "武汉解封");
		Resource 浙江湖南广东相继启动重大公共突发卫生事件一级响应 = myMod.createResource(xgfy + "浙江湖南广东相继启动重大公共突发卫生事件一级响应");
		Resource 山东浙江多人因监狱内疫情防控不力被免职 = myMod.createResource(xgfy + "山东浙江多人因监狱内疫情防控不力被免职");
		Resource 世卫组织将新型冠状病毒列为国际关注的突发公共卫生事件 = myMod.createResource(xgfy + "世卫组织将新型冠状病毒列为国际关注的突发公共卫生事件");
		Resource IOC允许将东京奥运会推迟至年底举行 = myMod.createResource(xgfy + "IOC允许将东京奥运会推迟至年底举行");
		Resource 北京深圳等地出现境外输入性病例 = myMod.createResource(xgfy + "北京深圳等地出现境外输入性病例");
		Resource 湖北单日新增确诊病例破万 = myMod.createResource(xgfy + "湖北单日新增确诊病例破万");
		Resource 上海北京广东三地确诊1例5例14例 = myMod.createResource(xgfy + "上海北京广东三地确诊1例5例14例");
		Resource 湖北省红十字会物资使用情况引发质疑 = myMod.createResource(xgfy + "湖北省红十字会物资使用情况引发质疑");
		Resource 科学防疫方式如戴口罩等受关注 = myMod.createResource(xgfy + "科学防疫方式如戴口罩等受关注");
		Resource 东京奥运会面临取消引关注 = myMod.createResource(xgfy + "东京奥运会面临取消引关注");
		//设置属性
		Property 对象要素 = myMod.createProperty(xgfy + "对象要素");
		Property 地点要素 = myMod.createProperty(xgfy + "地点要素");
		Property 关键用户 = myMod.createProperty(xgfy + "关键用户");
		
		//设置属性值
		Resource 头条新闻 = myMod.createResource(xgfy + "头条新闻");
		Resource 黄石市 = myMod.createResource(xgfy + "黄石市");
		Resource 武汉市 = myMod.createResource(xgfy + "武汉市");
		//设置三元组
        myMod.add(新冠肺炎, 因果关系, 国家政策和举措);
        myMod.add(国家政策和举措, 并发关系, 湖北省政策和举措);
        myMod.add(湖北省政策和举措, 并发关系, 其他省市政策和举措);
        myMod.add(其他省市政策和举措, 并发关系, 国际举措);
        myMod.add(国际举措, 并发关系, 疫情变化);
        myMod.add(疫情变化, 并发关系, 社会关注问题);
        
     
        
        myMod.add(国务院2020年4月4日举行全国性哀悼活动, 组成关系, 湖北省政策和举措);
        myMod.add(党中央成立应对疫情工作领导小组, 组成关系, 湖北省政策和举措);
        myMod.add(湖北省启动突发公共事件一级响应, 组成关系, 国家政策和举措);
        myMod.add(湖北省红十字会3名领导被问责, 组成关系, 湖北省政策和举措);
        myMod.add(在2020年湖北省两会召开, 组成关系, 湖北省政策和举措);
        myMod.add(武汉宣布封城, 组成关系, 武汉市政策和举措);
        myMod.add(武汉新建两所医院火神山和雷神山, 组成关系, 武汉市政策和举措);
//        myMod.add(武汉解封, 组成关系, 武汉市政策和举措);
        myMod.add(浙江湖南广东相继启动重大公共突发卫生事件一级响应, 组成关系, 其他省市政策和举措);
        myMod.add(山东浙江多人因监狱内疫情防控不力被免职, 组成关系, 其他省市政策和举措);
        myMod.add(世卫组织将新型冠状病毒列为国际关注的突发公共卫生事件, 组成关系, 国际举措);
        myMod.add(IOC允许将东京奥运会推迟至年底举行, 组成关系, 国际举措);
        myMod.add(北京深圳等地出现境外输入性病例, 组成关系, 疫情变化);
        myMod.add(湖北单日新增确诊病例破万, 组成关系, 疫情变化);
        myMod.add(上海北京广东三地确诊1例5例14例, 组成关系, 疫情变化);
        myMod.add(湖北省红十字会物资使用情况引发质疑, 组成关系, 社会关注问题);
        myMod.add(科学防疫方式如戴口罩等受关注, 组成关系, 社会关注问题);
        myMod.add(东京奥运会面临取消引关注, 组成关系, 社会关注问题);
        myMod.add(湖北省红十字会3名领导被问责, 跟随关系, 湖北省红十字会物资使用情况引发质疑);
        myMod.add(武汉宣布封城, 跟随关系, 湖北省启动突发公共事件一级响应);
//        myMod.add(武汉解封, 跟随关系, 国务院2020年4月4日举行全国性哀悼活动);
        myMod.add(IOC允许将东京奥运会推迟至年底举行, 跟随关系, 东京奥运会面临取消引关注);
        myMod.add(党中央成立应对疫情工作领导小组, 跟随关系, 武汉新建两所医院火神山和雷神山);
        
        
        myMod.add(国家政策和举措, 组成关系, 新冠肺炎);
        myMod.add(湖北省政策和举措, 组成关系, 新冠肺炎);
        myMod.add(武汉市政策和举措, 组成关系, 新冠肺炎);
        myMod.add(其他省市政策和举措, 组成关系, 新冠肺炎);
        myMod.add(国际举措, 组成关系, 新冠肺炎);
        myMod.add(疫情变化, 组成关系, 新冠肺炎);
        myMod.add(社会关注问题, 组成关系, 新冠肺炎);
         
        myMod.add(关键用户, 组成关系, 对象要素);
        
        myMod.add(黄石市, 并列关系, 武汉市);
        
        //属性
        myMod.add(东京奥运会面临取消引关注, 关键用户, 头条新闻);
        myMod.add(湖北省红十字会物资使用情况引发质疑, 关键用户, 头条新闻);
        myMod.add(武汉市政策和举措, 地点要素, 武汉市);
        myMod.add(黄石市政策和举措, 地点要素, 黄石市);
        
        PrintUtil.registerPrefix("", xgfy);
//         //输出当前模型
//      StmtIterator i = myMod.listStatements(null,null,(RDFNode)null);
//      while (i.hasNext()) {
//          System.out.println(" - " + PrintUtil.print(i.nextStatement()));
//      }
     
      GenericRuleReasoner reasoner = (GenericRuleReasoner) GenericRuleReasonerFactory.theInstance().create(null);
      reasoner.setRules(Rule.parseRules(
              "[ruleHoldShare: (?a1 :并列关系 ?a2) (?E :地点要素 ?a1) (?D :地点要素 ?a2) (?c2 :组成关系 ?D) -> (?E :可参考 ?c2) ] \n"
              +"[ruleHoldShare: (?A :跟随关系 ?B) (?B :关键用户 ?c)  -> (?A :关键用户 ?c)] \n"          
    		  ));
      reasoner.setMode(GenericRuleReasoner.HYBRID);
      InfGraph infgraph = reasoner.bind(myMod.getGraph());
      infgraph.setDerivationLogging(true);

      System.out.println("推理后...\n");

      Iterator<Triple> tripleIterator = infgraph.find(null, null, null);
      while (tripleIterator.hasNext()) {
          System.out.println(" - " + PrintUtil.print(tripleIterator.next()));
      }
	}

}
