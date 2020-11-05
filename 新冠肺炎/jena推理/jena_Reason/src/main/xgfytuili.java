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
		//�����¼���
		Resource �¹ڷ��� = myMod.createResource(xgfy + "�¹ڷ���");
		Resource ����仯 = myMod.createResource(xgfy + "����仯");
		Resource �������ߺ;ٴ� = myMod.createResource(xgfy + "�������ߺ;ٴ�");
		Resource ����ʡ���ߺ;ٴ� = myMod.createResource(xgfy + "����ʡ���ߺ;ٴ�");
		Resource �人�����ߺ;ٴ� = myMod.createResource(xgfy + "�人�����ߺ;ٴ�");
		Resource ����ʡ�����ߺ;ٴ� = myMod.createResource(xgfy + "����ʡ�����ߺ;ٴ�");
		Resource ���ʾٴ� = myMod.createResource(xgfy + "���ʾٴ�");
		Resource ����ע���� = myMod.createResource(xgfy + "����ע����");
		
		//��������
		Resource ��ʯ�����ߺ;ٴ� = myMod.createResource(xgfy + "��ʯ�����ߺ;ٴ�");
		
		
		//���ù�ϵ
		Property ���й�ϵ = myMod.createProperty(xgfy + "���й�ϵ");
		Property ��ɹ�ϵ = myMod.createProperty(xgfy + "��ɹ�ϵ");
		Property �����ϵ = myMod.createProperty(xgfy + "�����ϵ");
		Property �����ϵ = myMod.createProperty(xgfy + "�����ϵ");
		Property ������ϵ = myMod.createProperty(xgfy + "������ϵ");
		//�����¼�
		Resource ����Ժ2020��4��4�վ���ȫ���԰���� = myMod.createResource(xgfy + "����Ժ2020��4��4�վ���ȫ���԰����");
		Resource ���������Ӧ�����鹤���쵼С�� = myMod.createResource(xgfy + "���������Ӧ�����鹤���쵼С��");
		Resource ����ʡ����ͻ�������¼�һ����Ӧ = myMod.createResource(xgfy + "����ʡ����ͻ�������¼�һ����Ӧ");
		Resource ����ʡ��ʮ�ֻ�3���쵼������ = myMod.createResource(xgfy + "����ʡ��ʮ�ֻ�3���쵼������");
		Resource ��2020�����ʡ�����ٿ� = myMod.createResource(xgfy + "��2020�����ʡ�����ٿ�");
		Resource �人������� = myMod.createResource(xgfy + "�人�������");
		Resource �人�½�����ҽԺ����ɽ������ɽ = myMod.createResource(xgfy + "�人�½�����ҽԺ����ɽ������ɽ");
//		Resource �人��� = myMod.createResource(xgfy + "�人���");
		Resource �㽭���Ϲ㶫��������ش󹫹�ͻ�������¼�һ����Ӧ = myMod.createResource(xgfy + "�㽭���Ϲ㶫��������ش󹫹�ͻ�������¼�һ����Ӧ");
		Resource ɽ���㽭�����������������ز�������ְ = myMod.createResource(xgfy + "ɽ���㽭�����������������ز�������ְ");
		Resource ������֯�����͹�״������Ϊ���ʹ�ע��ͻ�����������¼� = myMod.createResource(xgfy + "������֯�����͹�״������Ϊ���ʹ�ע��ͻ�����������¼�");
		Resource IOC�����������˻��Ƴ�����׾��� = myMod.createResource(xgfy + "IOC�����������˻��Ƴ�����׾���");
		Resource �������ڵȵس��־��������Բ��� = myMod.createResource(xgfy + "�������ڵȵس��־��������Բ���");
		Resource ������������ȷ�ﲡ������ = myMod.createResource(xgfy + "������������ȷ�ﲡ������");
		Resource �Ϻ������㶫����ȷ��1��5��14�� = myMod.createResource(xgfy + "�Ϻ������㶫����ȷ��1��5��14��");
		Resource ����ʡ��ʮ�ֻ�����ʹ������������� = myMod.createResource(xgfy + "����ʡ��ʮ�ֻ�����ʹ�������������");
		Resource ��ѧ���߷�ʽ������ֵ��ܹ�ע = myMod.createResource(xgfy + "��ѧ���߷�ʽ������ֵ��ܹ�ע");
		Resource �������˻�����ȡ������ע = myMod.createResource(xgfy + "�������˻�����ȡ������ע");
		//��������
		Property ����Ҫ�� = myMod.createProperty(xgfy + "����Ҫ��");
		Property �ص�Ҫ�� = myMod.createProperty(xgfy + "�ص�Ҫ��");
		Property �ؼ��û� = myMod.createProperty(xgfy + "�ؼ��û�");
		
		//��������ֵ
		Resource ͷ������ = myMod.createResource(xgfy + "ͷ������");
		Resource ��ʯ�� = myMod.createResource(xgfy + "��ʯ��");
		Resource �人�� = myMod.createResource(xgfy + "�人��");
		//������Ԫ��
        myMod.add(�¹ڷ���, �����ϵ, �������ߺ;ٴ�);
        myMod.add(�������ߺ;ٴ�, ������ϵ, ����ʡ���ߺ;ٴ�);
        myMod.add(����ʡ���ߺ;ٴ�, ������ϵ, ����ʡ�����ߺ;ٴ�);
        myMod.add(����ʡ�����ߺ;ٴ�, ������ϵ, ���ʾٴ�);
        myMod.add(���ʾٴ�, ������ϵ, ����仯);
        myMod.add(����仯, ������ϵ, ����ע����);
        
     
        
        myMod.add(����Ժ2020��4��4�վ���ȫ���԰����, ��ɹ�ϵ, ����ʡ���ߺ;ٴ�);
        myMod.add(���������Ӧ�����鹤���쵼С��, ��ɹ�ϵ, ����ʡ���ߺ;ٴ�);
        myMod.add(����ʡ����ͻ�������¼�һ����Ӧ, ��ɹ�ϵ, �������ߺ;ٴ�);
        myMod.add(����ʡ��ʮ�ֻ�3���쵼������, ��ɹ�ϵ, ����ʡ���ߺ;ٴ�);
        myMod.add(��2020�����ʡ�����ٿ�, ��ɹ�ϵ, ����ʡ���ߺ;ٴ�);
        myMod.add(�人�������, ��ɹ�ϵ, �人�����ߺ;ٴ�);
        myMod.add(�人�½�����ҽԺ����ɽ������ɽ, ��ɹ�ϵ, �人�����ߺ;ٴ�);
//        myMod.add(�人���, ��ɹ�ϵ, �人�����ߺ;ٴ�);
        myMod.add(�㽭���Ϲ㶫��������ش󹫹�ͻ�������¼�һ����Ӧ, ��ɹ�ϵ, ����ʡ�����ߺ;ٴ�);
        myMod.add(ɽ���㽭�����������������ز�������ְ, ��ɹ�ϵ, ����ʡ�����ߺ;ٴ�);
        myMod.add(������֯�����͹�״������Ϊ���ʹ�ע��ͻ�����������¼�, ��ɹ�ϵ, ���ʾٴ�);
        myMod.add(IOC�����������˻��Ƴ�����׾���, ��ɹ�ϵ, ���ʾٴ�);
        myMod.add(�������ڵȵس��־��������Բ���, ��ɹ�ϵ, ����仯);
        myMod.add(������������ȷ�ﲡ������, ��ɹ�ϵ, ����仯);
        myMod.add(�Ϻ������㶫����ȷ��1��5��14��, ��ɹ�ϵ, ����仯);
        myMod.add(����ʡ��ʮ�ֻ�����ʹ�������������, ��ɹ�ϵ, ����ע����);
        myMod.add(��ѧ���߷�ʽ������ֵ��ܹ�ע, ��ɹ�ϵ, ����ע����);
        myMod.add(�������˻�����ȡ������ע, ��ɹ�ϵ, ����ע����);
        myMod.add(����ʡ��ʮ�ֻ�3���쵼������, �����ϵ, ����ʡ��ʮ�ֻ�����ʹ�������������);
        myMod.add(�人�������, �����ϵ, ����ʡ����ͻ�������¼�һ����Ӧ);
//        myMod.add(�人���, �����ϵ, ����Ժ2020��4��4�վ���ȫ���԰����);
        myMod.add(IOC�����������˻��Ƴ�����׾���, �����ϵ, �������˻�����ȡ������ע);
        myMod.add(���������Ӧ�����鹤���쵼С��, �����ϵ, �人�½�����ҽԺ����ɽ������ɽ);
        
        
        myMod.add(�������ߺ;ٴ�, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(����ʡ���ߺ;ٴ�, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(�人�����ߺ;ٴ�, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(����ʡ�����ߺ;ٴ�, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(���ʾٴ�, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(����仯, ��ɹ�ϵ, �¹ڷ���);
        myMod.add(����ע����, ��ɹ�ϵ, �¹ڷ���);
         
        myMod.add(�ؼ��û�, ��ɹ�ϵ, ����Ҫ��);
        
        myMod.add(��ʯ��, ���й�ϵ, �人��);
        
        //����
        myMod.add(�������˻�����ȡ������ע, �ؼ��û�, ͷ������);
        myMod.add(����ʡ��ʮ�ֻ�����ʹ�������������, �ؼ��û�, ͷ������);
        myMod.add(�人�����ߺ;ٴ�, �ص�Ҫ��, �人��);
        myMod.add(��ʯ�����ߺ;ٴ�, �ص�Ҫ��, ��ʯ��);
        
        PrintUtil.registerPrefix("", xgfy);
//         //�����ǰģ��
//      StmtIterator i = myMod.listStatements(null,null,(RDFNode)null);
//      while (i.hasNext()) {
//          System.out.println(" - " + PrintUtil.print(i.nextStatement()));
//      }
     
      GenericRuleReasoner reasoner = (GenericRuleReasoner) GenericRuleReasonerFactory.theInstance().create(null);
      reasoner.setRules(Rule.parseRules(
              "[ruleHoldShare: (?a1 :���й�ϵ ?a2) (?E :�ص�Ҫ�� ?a1) (?D :�ص�Ҫ�� ?a2) (?c2 :��ɹ�ϵ ?D) -> (?E :�ɲο� ?c2) ] \n"
              +"[ruleHoldShare: (?A :�����ϵ ?B) (?B :�ؼ��û� ?c)  -> (?A :�ؼ��û� ?c)] \n"          
    		  ));
      reasoner.setMode(GenericRuleReasoner.HYBRID);
      InfGraph infgraph = reasoner.bind(myMod.getGraph());
      infgraph.setDerivationLogging(true);

      System.out.println("�����...\n");

      Iterator<Triple> tripleIterator = infgraph.find(null, null, null);
      while (tripleIterator.hasNext()) {
          System.out.println(" - " + PrintUtil.print(tripleIterator.next()));
      }
	}

}
